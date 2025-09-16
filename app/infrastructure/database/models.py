from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.infrastructure.database import Base
from app.infrastructure.database import TimestampMixin

post_tags = Table(
    'post_tags',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True),
)


class User(TimestampMixin, Base):
    """User table"""
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True,
    )
    hashed_password: Mapped[str] = mapped_column(String(256), nullable=False)


class Category(TimestampMixin, Base):
    """Category table"""
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    slug: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[str | None] = mapped_column(Text)

    posts: Mapped[list[Post]] = relationship(back_populates='category')


class Tag(TimestampMixin, Base):
    """Tag table"""
    __tablename__ = 'tags'

    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    slug: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    posts: Mapped[list[Post]] = relationship(
        secondary=post_tags,
        back_populates='tags',
    )


class Post(TimestampMixin, Base):
    """Post table"""
    __tablename__ = 'posts'

    category_id: Mapped[int | None] = mapped_column(ForeignKey('categories.id'))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(String(20), default='draft')  # draft/published
    published_at: Mapped[datetime | None] = mapped_column(DateTime)

    category: Mapped[Category | None] = relationship(back_populates='posts')
    tags: Mapped[list[Tag]] = relationship(
        secondary=post_tags,
        back_populates='posts',
    )
