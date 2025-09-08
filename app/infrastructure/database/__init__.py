import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from ..config import Config


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass


config = Config()

# Create database engine with configuration
engine = create_engine(
    config.SQLALCHEMY_DATABASE_URL,
    # SQLite specific configuration
    connect_args={"check_same_thread": False} if config.is_sqlite else {},
    # PostgreSQL specific configuration
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800,  # Recycle connections after 30 minutes
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
