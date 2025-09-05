# app/infrastructure/config.py
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DATABASE_USER = os.getenv("DATABASE_USER", "user")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "password")
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT = os.getenv("DATABASE_PORT", 5432)
    DATABASE_NAME = os.getenv("DATABASE_NAME", "mydatabase")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://"
        f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
        f"{DATABASE_HOST}:{DATABASE_PORT}/"
        f"{DATABASE_NAME}"
    )
