# app/infrastructure/config.py
import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    # API Configuration
    API_TITLE = os.getenv("API_TITLE", "Blog API")
    API_VERSION = os.getenv("API_VERSION", "1.0.0")
    API_PREFIX = os.getenv("API_PREFIX", "/api")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

    # Database Configuration
    SQLALCHEMY_DATABASE_URL = os.getenv(
        "SQLALCHEMY_DATABASE_URL",
        "sqlite:///./test.db",  # Default SQLite for development
    )

    # CORS Configuration
    CORS_ORIGINS = eval(os.getenv("CORS_ORIGINS", '["http://localhost:3000"]'))

    @property
    def is_sqlite(self) -> bool:
        """Check if using SQLite database"""
        return self.SQLALCHEMY_DATABASE_URL.startswith("sqlite")
