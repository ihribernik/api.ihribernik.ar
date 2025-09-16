from __future__ import annotations

from datetime import datetime
from datetime import timezone

from sqlalchemy import create_engine
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import sessionmaker

from ..config import Settings


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    """Mixin to add id, created_at and updated_at columns.
    Created_at and updated_at are UTC timezone.
    """

    id: Mapped[int] = mapped_column(primary_key=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )


config = Settings()

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False} if config.is_sqlite else {},
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
