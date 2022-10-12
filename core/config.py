import secrets

from pydantic import AnyHttpUrl, validator


class Settings():
    PROJECT_NAME: str = "HumanResources"
    API_V1_STR: str = "/api/v1"

    # Databases urls
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./data/sql_app.db"
    SQLALCHEMY_USERS_DATABASE_URL: str = "sqlite+aiosqlite:///./data/auth.db"

    SECRET_KEY: str = secrets.token_urlsafe(32)
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = ["*"]
    USERS_OPEN_REGISTRATION: bool = True

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


settings = Settings()
