from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", ".env.prod"),
        env_file_encoding="utf-8",
    )

    API_TITLE: str = "Blog API"
    API_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    DEBUG: bool = False

    DATABASE_USER: str = "username"
    DATABASE_PASSWORD: str = "password"
    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_NAME: str = "blogdb"

    SECRET_KEY: str = "mi_super_secreto"
    JWT_SECRET_KEY: str = "otro_secreto"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 * 24 * 60
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./test.db"

    CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    @property
    def is_sqlite(self) -> bool:
        """Check if using SQLite database"""
        return self.SQLALCHEMY_DATABASE_URL.startswith("sqlite")
