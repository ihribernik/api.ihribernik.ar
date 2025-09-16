from fastapi import Depends
from sqlalchemy.orm import Session

from app.infrastructure.dependencies.database import get_db
from app.infrastructure.repositories.sqlalchemy.category import (
    SqlAlchemyCategoryRepository,
)
from app.infrastructure.repositories.sqlalchemy.post import SqlAlchemyPostRepository
from app.infrastructure.repositories.sqlalchemy.user import SqlAlchemyUserRepository


def get_post_repository(db: Session = Depends(get_db)) -> SqlAlchemyPostRepository:
    """
    Dependency to provide a SQLAlchemyPostRepository with a session.
    """
    return SqlAlchemyPostRepository(db)


def get_category_repository(
    db: Session = Depends(get_db),
) -> SqlAlchemyCategoryRepository:
    """
    Dependency to provide a SQLAlchemyCategoryRepository with a session.
    """
    return SqlAlchemyCategoryRepository(db)


def get_user_repository(db: Session = Depends(get_db)) -> SqlAlchemyUserRepository:
    """
    Dependency to provide a SQLAlchemyUserRepository with a session.
    """
    return SqlAlchemyUserRepository(db)
