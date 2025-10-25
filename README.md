# 🌈 Bifrost# 🌈 Bifrost# 🌈 Bifrost



> **The Rainbow Bridge for MLOps** - AI-powered log analysis platform



[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)> **The Rainbow Bridge for MLOps** - AI-powered log analysis platform**The Rainbow Bridge for MLOps** - AI-powered log analysis CLI

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg)](https://fastapi.tiangolo.com)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)## v0.1 - "미드가르드" (Local & Cloud Ready)

**Bifrost**는 MLOps 환경의 로그를 AI로 자동 분석하는 프로덕션급 플랫폼입니다.  

Kubernetes, CI/CD 파이프라인, 마이크로서비스 로그를 AI로 빠르게 분석하고 인사이트를 얻으세요.[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)



---[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg)](https://fastapi.tiangolo.com)Bifrost는 로컬(Ollama) 및 클라우드(AWS Bedrock) 두 가지 모드로 작동하는 AI 기반 로그 분석 도구입니다.



## ✨ Features[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)



### 🚀 Core## ✨ Features

- ✅ **Hybrid LLM**: Ollama (로컬) + AWS Bedrock (클라우드)

- ✅ **배치 처리**: 수백 개 로그 파일 동시 분석 (비동기)**Bifrost**는 MLOps 환경의 로그를 AI로 자동 분석하는 프로덕션급 플랫폼입니다.  

- ✅ **스트리밍**: 실시간 분석 결과 (WebSocket)

- ✅ **캐싱**: SHA256 해시 기반 중복 분석 방지Kubernetes, CI/CD 파이프라인, 마이크로서비스 로그를 AI로 빠르게 분석하고 인사이트를 얻으세요.- 🏠 **로컬 모드**: Ollama를 사용한 프라이버시 우선 분석



### 🎨 New Features (v0.2.1)- ☁️ **클라우드 모드**: AWS Bedrock (Claude 3) 프로덕션 스케일

- ✅ **Web UI**: Modern htmx-based interface with gradient design

- ✅ **Slack Integration**: Send analysis results to Slack channels---- � **스트리밍 출력**: 실시간 응답 확인

- ✅ **CSV/JSON Export**: Export analysis history in multiple formats

- ✅ **Log Filtering**: Filter by severity (ERROR/WARN/INFO), keywords, time range- ⚙️ **유연한 설정**: YAML 설정 파일 + 환경변수 지원

- ✅ **Real-time Statistics**: Log line counts by severity level

## ✨ Features- 🎨 **다양한 포맷**: Markdown, JSON, Plain text 출력

### 🔒 프로덕션 보안

- ✅ **API 키 인증**: 안전한 API 액세스- 🔧 **로그 전처리**: 크기 제한, 타임스탬프 제거, 자동 정리

- ✅ **Rate Limiting**: 시간당 요청 제한 (토큰 버킷)

- ✅ **입력 검증**: 크기 제한, XSS 방지, 형식 검증### 🚀 Core- 🔁 **재시도 로직**: 네트워크 불안정 대응

- ✅ **에러 핸들링**: 계층화된 예외 처리

- ✅ **CLI & REST API**: 터미널과 프로그래밍 방식 모두 지원

### 📊 관찰성

- ✅ **Prometheus 메트릭**: 7가지 커스텀 메트릭- ✅ **Hybrid LLM**: Ollama (로컬) + AWS Bedrock (클라우드)## �🚀 Quick Start

- ✅ **구조화된 로깅**: JSON 로그 (Elasticsearch 연동 가능)

- ✅ **헬스 체크**: Kubernetes liveness/readiness probes- ✅ **배치 처리**: 수백 개 로그 파일 동시 분석 (비동기)

- ✅ **Grafana 대시보드**: 실시간 모니터링

- ✅ **스트리밍**: 실시간 분석 결과 (WebSocket)### 1. 설치

### 🛠️ DevOps

- ✅ **Docker**: 멀티 스테이지 빌드 (최적화)- ✅ **캐싱**: SHA256 해시 기반 중복 분석 방지

- ✅ **Kubernetes**: HPA, ConfigMap, Secret

- ✅ **CI/CD**: GitHub Actions (테스트, 빌드, 배포)```bash

- ✅ **Makefile**: 원라인 개발 명령어

### 🔒 프로덕션 보안pip install -e .

---

- ✅ **API 키 인증**: 안전한 API 액세스

## 🚀 Quick Start

- ✅ **Rate Limiting**: 시간당 요청 제한 (토큰 버킷)# AWS Bedrock 사용 시 (선택)

### 1. 설치

```bash- ✅ **입력 검증**: 크기 제한, XSS 방지, 형식 검증pip install boto3

pip install -e .

- ✅ **에러 핸들링**: 계층화된 예외 처리```

# AWS Bedrock 사용 시 (선택)

pip install boto3

```

### 📊 관찰성### 2. Ollama 준비 (로컬 모드)

### 2. Ollama 준비 (로컬 모드)

```bash- ✅ **Prometheus 메트릭**: 7가지 커스텀 메트릭

# Ollama 설치 (https://ollama.ai)

ollama pull mistral- ✅ **구조화된 로깅**: JSON 로그 (Elasticsearch 연동 가능)```bash

ollama serve

```- ✅ **헬스 체크**: Kubernetes liveness/readiness probes# Ollama 설치 (https://ollama.ai)



### 3. Web UI 사용 (가장 빠른 방법 🎨)- ✅ **Grafana 대시보드**: 실시간 모니터링ollama pull mistral

```bash

# API 서버 실행ollama serve

uvicorn bifrost.api:app --reload

### 🛠️ DevOps```

# 브라우저에서 http://localhost:8000 접속

# 로그 붙여넣기 → 분석 클릭!- ✅ **Docker**: 멀티 스테이지 빌드 (최적화)

```

- ✅ **Kubernetes**: HPA, ConfigMap, Secret### 3. 사용

### 4. CLI 사용

```bash- ✅ **CI/CD**: GitHub Actions (테스트, 빌드, 배포)

# 로컬 모드 (Ollama)

bifrost local error.log- ✅ **Makefile**: 원라인 개발 명령어```bash

bifrost local --stream app.log

# 로컬 모드 (Ollama)

# 클라우드 모드 (AWS Bedrock)

bifrost cloud error.log---bifrost local error.log

bifrost cloud --region us-west-2 app.log

bifrost local --stream app.log

# 파이프 입력

kubectl logs my-pod | bifrost local## 🎯 Use Cases

docker logs my-container | bifrost cloud

# 클라우드 모드 (AWS Bedrock)

# 로그 필터링 ✨ NEW

bifrost filter-log app.log --severity ERROR### 1. Kubernetes 로그 분석bifrost cloud error.log

bifrost filter-log app.log --errors-only --output errors.log

```bashbifrost cloud --region us-west-2 app.log

# 결과 Export ✨ NEW

bifrost export --format csv --limit 100kubectl logs my-pod | bifrost local

bifrost export --format json --output results.json

```# 파이프 입력

# Slack 알림 ✨ NEW

bifrost slack --webhook-url https://hooks.slack.com/... --file app.logkubectl logs my-pod | bifrost local

bifrost slack --webhook-url https://hooks.slack.com/... --message "Deploy failed"

```### 2. CI/CD 실패 원인 파악docker logs my-container | bifrost cloud



---```bash



## 🎯 Use Cases# GitHub Actions 로그 다운로드# 출력 포맷 변경



### 1. Kubernetes 로그 분석gh run view 123456 --log > ci.logbifrost local --format json app.log

```bash

kubectl logs my-pod | bifrost localbifrost local --format plain error.log > analysis.txt

```

# Bifrost로 분석

### 2. CI/CD 실패 원인 파악

```bashbifrost local ci.log# 설정 파일 생성

# GitHub Actions

curl -H "Authorization: token $GITHUB_TOKEN" \```bifrost config --init

  https://api.github.com/repos/user/repo/actions/runs/123/logs | \

  bifrost cloudbifrost config --show

```

### 3. 배치 분석```

### 3. 마이크로서비스 배치 분석

```bash```bash

# 여러 서비스 로그 동시 분석

bifrost batch service1.log service2.log service3.log --concurrent 10# logs/ 디렉토리의 모든 로그 분석## 📦 구조

```

bifrost batch logs/*.log

### 4. Web UI로 실시간 분석

1. `uvicorn bifrost.api:app --reload` 실행``````

2. http://localhost:8000 접속

3. 로그 붙여넣기bifrost/

4. 심각도 필터 선택 (ERROR만 보기 등)

5. 분석 결과를 Slack으로 전송 (옵션)### 4. API 통합├── bifrost/



---```python│   ├── __init__.py



## 📡 REST APIimport httpx│   ├── main.py          # CLI 진입점



### 분석 엔드포인트│   ├── ollama.py        # Ollama 클라이언트

```bash

# 기본 분석response = httpx.post(│   ├── bedrock.py       # AWS Bedrock 클라이언트

curl -X POST http://localhost:8000/api/analyze \

  -H "X-API-Key: your-api-key" \    "http://localhost:8000/analyze",│   ├── config.py        # 설정 관리

  -H "Content-Type: application/json" \

  -d '{    json={"log_content": log_data, "source": "local"},│   ├── preprocessor.py  # 로그 전처리

    "log_content": "ERROR: Connection failed",

    "source": "local",    headers={"X-API-Key": "your-key"}│   └── formatter.py     # 출력 포맷터

    "service_name": "my-service"

  }')├── examples/



# 스트리밍 분석print(response.json()["response"])│   └── sample.log       # 테스트용 로그

curl -N http://localhost:8000/api/analyze/stream \

  -H "X-API-Key: your-api-key" \```├── requirements.txt

  -H "Content-Type: application/json" \

  -d '{"log_content": "..."}'├── setup.py

```

---├── bifrost.yaml.example # 설정 예시

### 필터링 & Export ✨ NEW

```bash└── README.md

# 심각도 필터링

curl -X POST http://localhost:8000/api/filter/severity \## 🚀 Quick Start```

  -H "X-API-Key: your-api-key" \

  -H "Content-Type: application/json" \

  -d '{

    "log_content": "INFO: Started\nERROR: Failed\nWARN: Slow",### Option 1: Docker Compose (권장)## ⚙️ 설정

    "min_level": "ERROR"

  }'



# CSV Export```bash### 설정 파일 (bifrost.yaml)

curl http://localhost:8000/api/export/csv?limit=100 \

  -H "X-API-Key: your-api-key" \# 1. 저장소 클론

  -o results.csv

git clone https://github.com/joeylife94/bifrost.git```bash

# JSON Export

curl http://localhost:8000/api/export/json?limit=50&pretty=true \cd bifrost# 샘플 생성

  -H "X-API-Key: your-api-key" \

  -o results.jsonbifrost config --init



# Slack 전송# 2. 전체 스택 시작 (6개 서비스)

curl -X POST http://localhost:8000/api/slack/send \

  -H "X-API-Key: your-api-key" \docker-compose up -d# 설정 확인

  -H "Content-Type: application/json" \

  -d '{bifrost config --show

    "webhook_url": "https://hooks.slack.com/...",

    "result": {...},# 3. API 접속```

    "service_name": "production-api"

  }'open http://localhost:8000/docs

```

```설정 파일 위치 (우선순위):

### 관리 엔드포인트

```bash1. `./bifrost.yaml`

# 히스토리 조회

curl http://localhost:8000/api/history?limit=10 \**포함된 서비스:**2. `./.bifrost.yaml`

  -H "X-API-Key: your-api-key"

- Bifrost API (port 8000)3. `~/.config/bifrost/config.yaml`

# 메트릭 조회

curl http://localhost:8000/api/metrics \- PostgreSQL (port 5432)4. `~/.bifrost.yaml`

  -H "X-API-Key: your-api-key"

- Redis (port 6379)

# Prometheus 메트릭

curl http://localhost:8000/metrics- Ollama (port 11434)### 환경변수



# 헬스 체크- Prometheus (port 9090)

curl http://localhost:8000/health

curl http://localhost:8000/health/live- Grafana (port 3001)```bash

curl http://localhost:8000/health/ready

export BIFROST_OLLAMA_URL=http://localhost:11434

# 시스템 정보

curl http://localhost:8000/system/info### Option 2: 로컬 개발export BIFROST_OLLAMA_MODEL=llama2

```

export BIFROST_BEDROCK_REGION=us-west-2

---

```bashexport BIFROST_BEDROCK_MODEL=anthropic.claude-3-sonnet-20240229-v1:0

## 🏗️ Architecture

# 1. 가상환경 생성```

```

┌─────────────────────────────────────────────────────────────┐python -m venv venv

│                      Bifrost Platform                        │

├─────────────────────────────────────────────────────────────┤source venv/bin/activate  # Windows: venv\Scripts\activate## 🎯 Roadmap

│                                                              │

│  ┌───────────┐  ┌───────────┐  ┌───────────┐               │

│  │  Web UI   │  │    CLI    │  │  REST API │               │

│  │  (htmx)   │  │  (Typer)  │  │ (FastAPI) │               │# 2. 의존성 설치- [x] v0.1: Local mode (Ollama)

│  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘               │

│        │              │              │                      │pip install -r requirements.txt- [x] v0.1: Cloud mode (AWS Bedrock) - 준비 완료

│        └──────────────┴──────────────┘                      │

│                       │                                     │- [x] v0.1: Config file support

│        ┌──────────────┴──────────────┐                      │

│        │                             │                      │# 3. Ollama 시작- [x] v0.1: Streaming output

│  ┌─────▼─────┐              ┌────────▼────────┐             │

│  │  Ollama   │              │  AWS Bedrock    │             │ollama serve- [x] v0.1: Log preprocessing

│  │  (Local)  │              │  (Claude 3)     │             │

│  └───────────┘              └─────────────────┘             │- [x] v0.1: Multiple output formats

│                                                              │

│  ┌──────────────────────────────────────────────┐           │# 4. CLI 사용- [ ] v0.2: 배치 분석 (여러 파일)

│  │           Data Layer                          │           │

│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐   │           │bifrost local error.log- [ ] v0.2: 커스텀 프롬프트

│  │  │PostgreSQL│  │  Redis   │  │   File   │   │           │

│  │  │   (DB)   │  │ (Cache)  │  │  Cache   │   │           │- [ ] v0.3: 웹 UI

│  │  └──────────┘  └──────────┘  └──────────┘   │           │

│  └──────────────────────────────────────────────┘           │# 5. API 서버 시작- [ ] v0.3: 히스토리 관리

│                                                              │

│  ┌──────────────────────────────────────────────┐           │uvicorn bifrost.api:app --reload

│  │           Observability                       │           │

│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐   │           │```## 📝 Examples

│  │  │Prometheus│  │  Grafana │  │   Logs   │   │           │

│  │  └──────────┘  └──────────┘  └──────────┘   │           │

│  └──────────────────────────────────────────────┘           │

│                                                              │---### 샘플 로그 분석

│  ┌──────────────────────────────────────────────┐           │

│  │           Integrations ✨ NEW                 │           │

│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐   │           │

│  │  │  Slack   │  │   CSV    │  │  JSON    │   │           │## 📖 Documentation```bash

│  │  └──────────┘  └──────────┘  └──────────┘   │           │

│  └──────────────────────────────────────────────┘           │bifrost local examples/sample.log

└─────────────────────────────────────────────────────────────┘

```| 문서 | 설명 |```



---|------|------|



## 📊 Monitoring| **[PORTFOLIO.md](PORTFOLIO.md)** | 프로젝트 동기, 기술 의사결정, 증명된 역량 |### Kubernetes 로그



### Prometheus 메트릭| **[ARCHITECTURE.md](ARCHITECTURE.md)** | 시스템 아키텍처, 설계 패턴, 확장성 전략 |

- `bifrost_requests_total`: 총 요청 수 (by source, status)

- `bifrost_request_duration_seconds`: 요청 처리 시간| **[TECHNICAL.md](TECHNICAL.md)** | API 레퍼런스, 배포 가이드, 트러블슈팅 |```bash

- `bifrost_analysis_errors_total`: 분석 에러 수

- `bifrost_cache_hits_total`: 캐시 히트 수| **[COMPLETION.md](COMPLETION.md)** | 구현 체크리스트, 기술 스택, 다음 단계 |kubectl logs -f deployment/my-app | bifrost local --stream

- `bifrost_active_requests`: 현재 처리 중인 요청

- `bifrost_log_size_bytes`: 로그 크기 (히스토그램)| **[CHANGELOG.md](CHANGELOG.md)** | 최신 업데이트 및 변경사항 |```

- `bifrost_rate_limit_exceeded_total`: Rate limit 초과 횟수



### Grafana 대시보드

```bash---### Docker 컨테이너 로그

# Grafana 실행 (Docker Compose)

docker-compose up -d grafana



# http://localhost:3000 접속## 🏗️ Architecture```bash

# 대시보드 import: grafana/dashboard.json

```docker logs my-container 2>&1 | bifrost cloud



---``````



## 🧪 Development┌─────────────────────────────────────────────────────────┐



### 1. 개발 환경 설정│                   Client Layer                          │### CI/CD 파이프라인

```bash

# 저장소 클론│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │

git clone https://github.com/joeylife94/bifrost.git

cd bifrost│  │   CLI    │  │  WebUI   │  │  API     │             │```bash



# 의존성 설치│  └──────────┘  └──────────┘  └──────────┘             │# JSON 출력으로 파싱 가능

make install

└─────────────────────────────────────────────────────────┘bifrost local build.log --format json | jq '.response'

# 개발 모드 실행

make run                        ↓```

```

┌─────────────────────────────────────────────────────────┐

### 2. 테스트

```bash│              Presentation (FastAPI)                     │## 🔧 개발

# 전체 테스트 실행

make test│  - Rate Limiting, Auth, Validation                      │



# 커버리지 포함└─────────────────────────────────────────────────────────┘```bash

make test-coverage

                        ↓# 개발 모드 설치

# 특정 테스트만

pytest tests/test_api.py -v┌─────────────────────────────────────────────────────────┐pip install -e .

```

│            Business Logic                               │

### 3. 코드 품질

```bash│  - Preprocessor, Analyzer, Formatter                    │# 의존성 설치

# Linting

make lint└─────────────────────────────────────────────────────────┘pip install -r requirements.txt



# 포맷팅                        ↓```

make format

┌─────────────────────────────────────────────────────────┐

# 타입 체크

make typecheck│           Integration (LLM, DB)                         │---

```

│  - Ollama Client, Bedrock Client, Database              │

### 4. Docker

```bash└─────────────────────────────────────────────────────────┘**Built with 🔨 by vibe coding**

# 이미지 빌드

make docker-build                        ↓

┌─────────────────────────────────────────────────────────┐

# 컨테이너 실행│         Infrastructure                                  │

make docker-run│  - PostgreSQL, Redis, Prometheus                        │

└─────────────────────────────────────────────────────────┘

# Docker Compose 전체 스택```

make docker-compose-up

```**상세**: [ARCHITECTURE.md](ARCHITECTURE.md)



### 5. Kubernetes---

```bash

# 배포## 💻 CLI Usage

make k8s-deploy

### 로컬 분석 (Ollama)

# 상태 확인```bash

make k8s-status# 파일 분석

bifrost local error.log

# 로그 확인

make k8s-logs# stdin 분석

cat error.log | bifrost local

# 삭제

make k8s-delete# 스트리밍 모드

```bifrost local error.log --stream



---# 마크다운 출력

bifrost local error.log --format markdown

## 📚 Documentation```



- [ARCHITECTURE.md](ARCHITECTURE.md) - 시스템 아키텍처 상세 설명### 클라우드 분석 (AWS Bedrock)

- [PORTFOLIO.md](PORTFOLIO.md) - 프로젝트 포트폴리오 문서```bash

- [CHANGELOG.md](CHANGELOG.md) - 버전별 변경 사항# AWS 설정 필요

- [COMPLETION.md](COMPLETION.md) - 향후 로드맵export AWS_PROFILE=your-profile

- [API Documentation](http://localhost:8000/docs) - Swagger UI (서버 실행 후)

bifrost cloud error.log

---```



## 🤝 Contributing### 배치 분석

```bash

1. Fork the repository# 여러 파일 동시 분석

2. Create your feature branch (`git checkout -b feature/amazing`)bifrost batch logs/*.log

3. Commit your changes (`git commit -m 'Add amazing feature'`)

4. Push to the branch (`git push origin feature/amazing`)# 결과를 파일로 저장

5. Open a Pull Requestbifrost batch logs/*.log > report.md

```

---

---

## 📝 License

## 🌐 API Usage

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 1. 로그 분석

---```bash

curl -X POST http://localhost:8000/analyze \

## 🙏 Acknowledgments  -H "X-API-Key: your-key" \

  -H "Content-Type: application/json" \

- [Ollama](https://ollama.ai) - Local LLM inference  -d '{

- [AWS Bedrock](https://aws.amazon.com/bedrock/) - Claude 3 API    "log_content": "ERROR: Connection refused",

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework    "source": "local",

- [htmx](https://htmx.org/) - Modern web UI interactions    "service_name": "my-api"

- [Prometheus](https://prometheus.io/) - Monitoring and alerting  }'

```

---

### 2. 분석 히스토리 조회

## 📧 Contact```bash

curl http://localhost:8000/history?limit=10 \

- GitHub: [@joeylife94](https://github.com/joeylife94)  -H "X-API-Key: your-key"

- Project: [Bifrost](https://github.com/joeylife94/bifrost)```



---### 3. 메트릭 확인

```bash

Made with ❤️ for MLOps Engineers# Prometheus 메트릭

curl http://localhost:8000/metrics/prometheus

# 내부 메트릭
curl http://localhost:8000/metrics
```

### 4. WebSocket 스트리밍
```python
import asyncio
import websockets

async def stream_analysis():
    async with websockets.connect("ws://localhost:8000/ws/analyze") as ws:
        await ws.send('{"log_content": "ERROR log"}')
        async for msg in ws:
            print(msg)

asyncio.run(stream_analysis())
```

**전체 API 문서**: http://localhost:8000/docs

---

## 🔧 Configuration

### 환경변수
```bash
# Database
DATABASE_URL=postgresql://user:pass@localhost/bifrost

# Ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral

# AWS Bedrock (optional)
AWS_REGION=us-east-1
BEDROCK_MODEL_ID=anthropic.claude-3-sonnet-20240229-v1:0

# Rate Limiting
RATE_LIMIT_PER_HOUR=100

# Logging
LOG_LEVEL=INFO
```

### bifrost.yaml
```yaml
database:
  url: "sqlite:///bifrost.db"

ollama:
  base_url: "http://localhost:11434"
  model: "mistral"
  timeout: 300

bedrock:
  region: "us-east-1"
  model_id: "anthropic.claude-3-sonnet-20240229-v1:0"

api:
  rate_limit: 100
  cache_ttl_hours: 24
```

---

## 📊 Monitoring

### Prometheus 메트릭

| 메트릭 | 타입 | 설명 |
|--------|------|------|
| `bifrost_analysis_total` | Counter | 총 분석 요청 수 |
| `bifrost_analysis_duration_seconds` | Histogram | 분석 소요 시간 |
| `bifrost_cache_hits_total` | Counter | 캐시 히트 수 |
| `bifrost_cache_misses_total` | Counter | 캐시 미스 수 |
| `bifrost_errors_total` | Counter | 에러 발생 수 |
| `bifrost_active_requests` | Gauge | 진행 중 요청 수 |
| `bifrost_llm_tokens_total` | Counter | 사용한 토큰 수 |

### Grafana 대시보드

```bash
# Grafana 열기 (Docker Compose 실행 시)
open http://localhost:3001

# 기본 계정: admin/admin
```

---

## 🧪 Testing

```bash
# 전체 테스트
pytest tests/ -v

# 커버리지 포함
pytest tests/ --cov=bifrost --cov-report=html

# 특정 테스트만
pytest tests/test_api.py -v
```

**현재 커버리지**: 85%+

---

## 🚀 Deployment

### Docker

```bash
# 이미지 빌드
docker build -t bifrost:latest .

# 컨테이너 실행
docker run -p 8000:8000 bifrost:latest
```

### Kubernetes

```bash
# ConfigMap & Secret 적용
kubectl apply -f k8s/config.yaml

# 배포
kubectl apply -f k8s/deployment.yaml

# 상태 확인
kubectl get pods -l app=bifrost
```

### CI/CD (GitHub Actions)

`.github/workflows/ci.yml`이 자동으로:
1. 테스트 실행
2. Docker 이미지 빌드
3. 이미지 푸시 (GitHub Container Registry)
4. Kubernetes 배포

---

## 🛠️ Development

### 주요 명령어

```bash
# 설치 & 설정
pip install -r requirements.txt  # 의존성 설치
python -m bifrost.main --help    # CLI 도움말

# 실행
uvicorn bifrost.api:app --reload # API 서버 (개발 모드)
python -m bifrost.main local     # CLI 로컬 모드

# 테스트 & 검증
pytest tests/ -v                 # 테스트
black bifrost/ tests/            # 포맷
flake8 bifrost/                  # 린트

# Docker
docker-compose up -d             # 전체 스택 시작
docker-compose logs -f           # 로그 확인
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

**코드 스타일**: Black, Flake8  
**테스트**: pytest (필수)

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

---

## 👨‍💻 Author

**Joey**  
MLOps & Backend Engineer  
[@joeylife94](https://github.com/joeylife94)

---

## 🙏 Acknowledgments

- **Ollama**: 로컬 LLM 런타임
- **AWS Bedrock**: Claude 3 제공
- **FastAPI**: 훌륭한 웹 프레임워크
- **SQLAlchemy**: 강력한 ORM

---

## 🎯 Roadmap

### v0.3 (계획)
- [ ] 웹 UI (React + shadcn/ui)
- [ ] MLflow 연동 (프롬프트 실험)
- [ ] RAG (과거 분석 결과 활용)

### v0.4 (계획)
- [ ] Slack/Discord 통합
- [ ] 커스텀 프롬프트 관리
- [ ] 이상 탐지 (Anomaly Detection)

### v1.0 (장기)
- [ ] SaaS 전환 (Multi-tenancy)
- [ ] Root Cause Analysis
- [ ] Auto-remediation

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/joeylife94/bifrost/issues)
- **Discussions**: [GitHub Discussions](https://github.com/joeylife94/bifrost/discussions)

---

<div align="center">

**Made with ❤️ for the MLOps Community**

[Documentation](TECHNICAL.md) • [Architecture](ARCHITECTURE.md) • [Portfolio](PORTFOLIO.md)

</div>
