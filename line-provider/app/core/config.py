import secrets
import base64
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SECRET_REFRESH_KEY: str = secrets.token_urlsafe(32)
    SESSION_SECRET: str
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8


    # 60 minutes * 24 hours * 7 days * 4 weeks * 12 month = 1 year
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 * 4 * 12

    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    # SERVER_STORAGE: str
    SERVER_TZ: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str
    PROJECT_VERSION: str

    SENTRY_DSN: Optional[HttpUrl] = None


    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()