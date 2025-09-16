from __future__ import annotations

from collections.abc import Generator

from app.infrastructure.database import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
