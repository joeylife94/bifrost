"""설정 관리 모듈"""

import os
from pathlib import Path
from typing import Optional, Dict, Any
import yaml


DEFAULT_CONFIG = {
    "ollama": {
        "url": "http://localhost:11434",
        "model": "mistral",
        "timeout": 120,
        "max_retries": 3,
    },
    "bedrock": {
        "region": "us-east-1",
        "model": "anthropic.claude-3-sonnet-20240229-v1:0",
        "profile": "default",
    },
    "log": {
        "max_size_mb": 5,
        "truncate": True,
        "remove_timestamps": False,
    },
    "output": {
        "format": "markdown",  # markdown, json, plain
        "color": True,
        "verbose": False,
    },
}


class Config:
    """설정 관리 클래스"""
    
    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or self._find_config()
        self.data = self._load_config()
    
    def _find_config(self) -> Optional[Path]:
        """설정 파일 자동 탐색"""
        search_paths = [
            Path.cwd() / "bifrost.yaml",
            Path.cwd() / ".bifrost.yaml",
            Path.home() / ".config" / "bifrost" / "config.yaml",
            Path.home() / ".bifrost.yaml",
        ]
        
        for path in search_paths:
            if path.exists():
                return path
        
        return None
    
    def _load_config(self) -> Dict[str, Any]:
        """설정 파일 로드"""
        config = DEFAULT_CONFIG.copy()
        
        if self.config_path and self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    user_config = yaml.safe_load(f) or {}
                    config = self._merge_config(config, user_config)
            except Exception as e:
                print(f"⚠️  설정 파일 로드 실패, 기본값 사용: {e}")
        
        # 환경변수 오버라이드
        config = self._apply_env_overrides(config)
        
        return config
    
    def _merge_config(self, base: Dict, override: Dict) -> Dict:
        """설정 병합 (재귀적)"""
        result = base.copy()
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._merge_config(result[key], value)
            else:
                result[key] = value
        return result
    
    def _apply_env_overrides(self, config: Dict) -> Dict:
        """환경변수로 설정 오버라이드"""
        # BIFROST_OLLAMA_URL 같은 형식
        if url := os.getenv("BIFROST_OLLAMA_URL"):
            config["ollama"]["url"] = url
        if model := os.getenv("BIFROST_OLLAMA_MODEL"):
            config["ollama"]["model"] = model
        if region := os.getenv("BIFROST_BEDROCK_REGION"):
            config["bedrock"]["region"] = region
        if bedrock_model := os.getenv("BIFROST_BEDROCK_MODEL"):
            config["bedrock"]["model"] = bedrock_model
        
        return config
    
    def get(self, path: str, default: Any = None) -> Any:
        """점 표기법으로 설정값 가져오기 (예: "ollama.url")"""
        keys = path.split(".")
        value = self.data
        
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
            else:
                return default
        
        return value if value is not None else default
    
    @classmethod
    def create_sample_config(cls, path: Path):
        """샘플 설정 파일 생성"""
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(DEFAULT_CONFIG, f, default_flow_style=False, allow_unicode=True)
