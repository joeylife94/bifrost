"""FastAPI REST API 서버"""

import time
from typing import Optional, List
from datetime import datetime

from fastapi import FastAPI, HTTPException, Depends, Header, BackgroundTasks, WebSocket, WebSocketDisconnect, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from bifrost.ollama import OllamaClient
from bifrost.bedrock import BedrockClient, is_bedrock_available
from bifrost.database import get_database, Database
from bifrost.preprocessor import LogPreprocessor
from bifrost.metrics import PrometheusMetrics
from bifrost.logger import logger
from bifrost.ratelimit import RateLimiter
from bifrost.exceptions import BifrostException, RateLimitError, handle_exception
from bifrost.validators import InputValidator
from bifrost.filters import LogFilter, SeverityLevel
from bifrost.export import DataExporter
from bifrost.slack import SlackNotifier

# FastAPI 앱
app = FastAPI(
    title="Bifrost API",
    description="🌈 The Rainbow Bridge for MLOps - AI-powered log analysis",
    version="0.2.0",
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에서는 제한 필요
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prometheus 메트릭
metrics = PrometheusMetrics()

# Rate Limiter 초기화
rate_limiter = RateLimiter(requests_per_hour=100)

# 전역 예외 핸들러
@app.exception_handler(BifrostException)
async def bifrost_exception_handler(request: Request, exc: BifrostException):
    logger.error(
        f"Bifrost error: {exc.message}",
        error_code=exc.code,
        path=str(request.url.path) if hasattr(request.url, 'path') else str(request.url)
    )
    return JSONResponse(
        status_code=400,
        content=handle_exception(exc)
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(
        f"Unhandled error: {str(exc)}",
        path=str(request.url.path) if hasattr(request.url, 'path') else str(request.url),
        exception_type=type(exc).__name__
    )
    return JSONResponse(
        status_code=500,
        content=handle_exception(exc)
    )


# ==================== Pydantic Models ====================

class AnalyzeRequest(BaseModel):
    """분석 요청"""
    log_content: str = Field(..., description="로그 내용")
    source: str = Field("local", description="분석 소스 (local/cloud)")
    model: Optional[str] = Field(None, description="모델명")
    service_name: Optional[str] = Field(None, description="서비스 이름")
    environment: Optional[str] = Field(None, description="환경 (prod/staging)")
    tags: Optional[List[str]] = Field(default_factory=list, description="태그")
    stream: bool = Field(False, description="스트리밍 모드")


class AnalyzeResponse(BaseModel):
    """분석 응답"""
    id: int
    response: str
    duration_seconds: float
    model: str
    cached: bool = False


class HistoryQuery(BaseModel):
    """히스토리 조회"""
    limit: int = Field(50, ge=1, le=500)
    offset: int = Field(0, ge=0)
    service_name: Optional[str] = None
    model: Optional[str] = None
    status: Optional[str] = None


class MetricsResponse(BaseModel):
    """메트릭 응답"""
    total_analyses: int
    avg_duration_seconds: float
    model_stats: List[dict]


# ==================== Dependencies ====================

async def verify_api_key(x_api_key: Optional[str] = Header(None)) -> bool:
    """API 키 검증"""
    if not x_api_key:
        return True  # 개발 모드: API 키 선택
    
    db = get_database()
    if not db.validate_api_key(x_api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    return True


# ==================== Routes ====================

@app.get("/")
async def root():
    """헬스 체크"""
    return {
        "name": "Bifrost API",
        "version": "0.2.0",
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
    }


@app.get("/health")
async def health():
    """상세 헬스 체크"""
    db = get_database()
    
    ollama_healthy = False
    try:
        client = OllamaClient()
        ollama_healthy = client.health_check()
    except:
        pass
    
    return {
        "status": "healthy",
        "components": {
            "database": "ok",
            "ollama": "ok" if ollama_healthy else "unavailable",
            "bedrock": "ok" if is_bedrock_available() else "not_configured",
        },
        "timestamp": datetime.utcnow().isoformat(),
    }


@app.post("/analyze", response_model=AnalyzeResponse, dependencies=[Depends(verify_api_key)])
async def analyze_log(request: AnalyzeRequest, background_tasks: BackgroundTasks):
    """로그 분석 API"""
    start_time = time.time()
    db = get_database()
    
    # 캐시 확인 (중복 분석 방지)
    import hashlib
    log_hash = hashlib.sha256(request.log_content.encode()).hexdigest()
    cached_results = db.get_duplicate_analyses(log_hash, hours=24)
    
    if cached_results and not request.stream:
        cached = cached_results[0]
        metrics.increment_cache_hits()
        return AnalyzeResponse(
            id=cached["id"],
            response=cached["response"],
            duration_seconds=cached["duration_seconds"],
            model=cached["model"],
            cached=True,
        )
    
    # 전처리
    preprocessor = LogPreprocessor()
    log_content = preprocessor.process(request.log_content)
    
    # 프롬프트
    from bifrost.main import MASTER_PROMPT
    prompt = MASTER_PROMPT.format(log_content=log_content)
    
    try:
        # 분석 실행
        if request.source == "local":
            client = OllamaClient(model=request.model or "mistral")
            result = client.analyze(prompt, stream=False)  # API는 스트리밍 미지원
        elif request.source == "cloud":
            if not is_bedrock_available():
                raise HTTPException(status_code=400, detail="Bedrock not available (boto3 not installed)")
            client = BedrockClient(model_id=request.model or "anthropic.claude-3-sonnet-20240229-v1:0")
            result = client.analyze(prompt)
        else:
            raise HTTPException(status_code=400, detail="Invalid source (local or cloud)")
        
        duration = time.time() - start_time
        
        # DB 저장 (백그라운드)
        analysis_id = db.save_analysis(
            source=request.source,
            model=result["metadata"]["model"],
            log_content=request.log_content,
            response=result["response"],
            duration=duration,
            tags=request.tags,
            service_name=request.service_name,
            environment=request.environment,
            tokens_used=result["metadata"].get("usage", {}).get("total_tokens"),
            status="completed",
        )
        
        # 메트릭 업데이트
        metrics.increment_analysis_count(request.source)
        metrics.observe_analysis_duration(duration, request.source)
        
        return AnalyzeResponse(
            id=analysis_id,
            response=result["response"],
            duration_seconds=round(duration, 2),
            model=result["metadata"]["model"],
            cached=False,
        )
    
    except Exception as e:
        # 에러 저장
        db.save_analysis(
            source=request.source,
            model=request.model or "unknown",
            log_content=request.log_content,
            response="",
            duration=time.time() - start_time,
            status="failed",
            error_message=str(e),
        )
        
        metrics.increment_error_count(request.source)
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@app.post("/history", response_model=List[dict])
async def get_history(query: HistoryQuery, _: bool = Depends(verify_api_key)):
    """분석 히스토리 조회"""
    db = get_database()
    results = db.list_analyses(
        limit=query.limit,
        offset=query.offset,
        service_name=query.service_name,
        model=query.model,
        status=query.status,
    )
    return results


@app.get("/history/{analysis_id}", response_model=dict)
async def get_analysis_detail(analysis_id: int, _: bool = Depends(verify_api_key)):
    """특정 분석 결과 조회"""
    db = get_database()
    result = db.get_analysis(analysis_id)
    if not result:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return result


@app.get("/metrics", response_model=MetricsResponse)
async def get_metrics(hours: int = 24, _: bool = Depends(verify_api_key)):
    """메트릭 조회"""
    db = get_database()
    summary = db.get_metrics_summary(hours=hours)
    return MetricsResponse(**summary)


@app.get("/metrics/prometheus")
async def get_prometheus_metrics():
    """Prometheus 메트릭 엔드포인트"""
    from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
    from fastapi.responses import Response
    
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.websocket("/ws/analyze")
async def websocket_analyze(websocket: WebSocket):
    """WebSocket 스트리밍 분석"""
    await websocket.accept()
    
    try:
        while True:
            # 요청 받기
            data = await websocket.receive_json()
            log_content = data.get("log_content", "")
            source = data.get("source", "local")
            model = data.get("model")
            
            if not log_content:
                await websocket.send_json({"error": "log_content is required"})
                continue
            
            # 전처리
            preprocessor = LogPreprocessor()
            log_content = preprocessor.process(log_content)
            
            from bifrost.main import MASTER_PROMPT
            prompt = MASTER_PROMPT.format(log_content=log_content)
            
            # 스트리밍 분석
            if source == "local":
                client = OllamaClient(model=model or "mistral")
                # TODO: WebSocket용 스트리밍 구현
                result = client.analyze(prompt, stream=False)
                await websocket.send_json({
                    "type": "complete",
                    "response": result["response"],
                    "metadata": result["metadata"],
                })
            else:
                await websocket.send_json({"error": "Cloud streaming not supported yet"})
    
    except WebSocketDisconnect:
        pass


@app.post("/api-keys", dependencies=[Depends(verify_api_key)])
async def create_api_key(name: str, rate_limit: int = 100, description: Optional[str] = None):
    """API 키 생성 (관리자용)"""
    db = get_database()
    key = db.create_api_key(name=name, rate_limit=rate_limit, description=description)
    return {"key": key, "name": name, "rate_limit": rate_limit}


@app.get("/api-keys", dependencies=[Depends(verify_api_key)])
async def list_api_keys():
    """API 키 목록"""
    db = get_database()
    return db.list_api_keys()


# ==================== Startup/Shutdown ====================

@app.on_event("startup")
async def startup_event():
    """서버 시작 시"""
    db = get_database()
    db.init_db()
    print("🌈 Bifrost API Server started!")


@app.on_event("shutdown")
async def shutdown_event():
    """서버 종료 시"""
    print("👋 Bifrost API Server shutting down...")


# ==================== 새로운 기능 엔드포인트 ====================

@app.get("/", response_class=HTMLResponse)
async def web_ui():
    """웹 UI (htmx)"""
    try:
        with open("static/index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Web UI not found. Please check static/index.html</h1>"


@app.post("/api/analyze-web")
async def analyze_web(
    log_content: str = Form(...),
    source: str = Form("local"),
    severity: str = Form(None),
    service_name: str = Form(None),
    environment: str = Form(None),
):
    """웹 UI용 분석 엔드포인트 (Form 데이터)"""
    try:
        # 심각도 필터링
        filtered_log = log_content
        if severity:
            filtered_log = LogFilter.filter_by_severity(
                log_content,
                min_level=SeverityLevel(severity)
            )
        
        # 분석 실행
        preprocessor = LogPreprocessor()
        processed_log = preprocessor.process(filtered_log)
        
        if source == "local":
            client = OllamaClient()
        else:
            client = BedrockClient()
        
        result = client.analyze(processed_log)
        
        # DB 저장
        db = get_database()
        analysis_id = db.save_analysis(
            log_content=log_content,
            response=result.get("response", ""),
            source=source,
            service_name=service_name,
            environment=environment,
        )
        
        # HTML 응답
        html = f"""
        <div class="result">
            <div class="alert alert-success">
                ✅ 분석 완료! (ID: {analysis_id})
            </div>
            <h3>📊 분석 결과</h3>
            <pre>{result.get('response', 'No response')}</pre>
            
            <div class="stats">
                <div class="stat-card">
                    <div class="number">{result.get('model', 'N/A')}</div>
                    <div class="label">모델</div>
                </div>
                <div class="stat-card">
                    <div class="number">{source}</div>
                    <div class="label">소스</div>
                </div>
                <div class="stat-card">
                    <div class="number">{service_name or 'N/A'}</div>
                    <div class="label">서비스</div>
                </div>
            </div>
        </div>
        """
        
        return HTMLResponse(content=html)
    
    except Exception as e:
        error_html = f"""
        <div class="result">
            <div class="alert alert-error">
                ❌ 에러 발생: {str(e)}
            </div>
        </div>
        """
        return HTMLResponse(content=error_html, status_code=400)


@app.get("/api/export/csv")
async def export_csv(
    limit: int = 100,
    api_key: str = Depends(verify_api_key)
):
    """분석 결과를 CSV로 export"""
    db = get_database()
    results = db.get_analysis_history(limit=limit)
    
    csv_content = DataExporter.to_csv(results)
    
    return StreamingResponse(
        iter([csv_content]),
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=bifrost_export_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
        }
    )


@app.get("/api/export/json")
async def export_json(
    limit: int = 100,
    pretty: bool = True,
    api_key: str = Depends(verify_api_key)
):
    """분석 결과를 JSON으로 export"""
    db = get_database()
    results = db.get_analysis_history(limit=limit)
    
    json_content = DataExporter.to_json(results, pretty=pretty)
    
    return StreamingResponse(
        iter([json_content]),
        media_type="application/json",
        headers={
            "Content-Disposition": f"attachment; filename=bifrost_export_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        }
    )


@app.post("/api/filter/severity")
async def filter_by_severity(
    log_content: str = Field(..., description="로그 내용"),
    min_level: SeverityLevel = Field(SeverityLevel.INFO, description="최소 심각도"),
    api_key: str = Depends(verify_api_key)
):
    """심각도로 필터링"""
    filtered = LogFilter.filter_by_severity(log_content, min_level)
    stats = LogFilter.get_log_statistics(filtered)
    
    return {
        "filtered_log": filtered,
        "statistics": stats
    }


@app.post("/api/filter/errors")
async def filter_errors_only(
    log_content: str = Field(..., description="로그 내용"),
    api_key: str = Depends(verify_api_key)
):
    """에러만 추출"""
    filtered = LogFilter.extract_errors_only(log_content)
    
    return {
        "filtered_log": filtered,
        "line_count": len(filtered.split('\n'))
    }


@app.post("/api/slack/send")
async def send_to_slack(
    webhook_url: str = Field(..., description="Slack Webhook URL"),
    result: dict = Field(..., description="분석 결과"),
    service_name: Optional[str] = None,
    api_key: str = Depends(verify_api_key)
):
    """분석 결과를 Slack으로 전송"""
    slack = SlackNotifier(webhook_url)
    success = slack.send_analysis_result(result, service_name)
    
    return {
        "success": success,
        "message": "Slack 전송 성공" if success else "Slack 전송 실패"
    }


@app.get("/api/log/stats")
async def get_log_statistics(
    log_content: str,
    api_key: str = Depends(verify_api_key)
):
    """로그 통계"""
    stats = LogFilter.get_log_statistics(log_content)
    
    return stats


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
