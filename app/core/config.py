from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", ".env.prod"),
        env_file_encoding="utf-8",
    )

    API_TITLE: str = "Blog API"
    API_VERSION: str = "1.0.0"
    API_PORT: int = 8000
    API_PREFIX: str = "/api"
    DEBUG: bool = False

    DATABASE_DRIVER: str = "postgresql"
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

    CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    @property
    def is_sqlite(self) -> bool:
        """Check if using SQLite database"""
        return self.connection_string.startswith("sqlite")

    @property
    def connection_string(self) -> str:
        """Return the connection string for SQLAlchemy"""
        return f"{self.DATABASE_DRIVER}://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
