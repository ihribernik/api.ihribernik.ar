from fastapi import Depends

from app.application.services.post import PostService
from app.infrastructure.dependencies.respository import get_post_repository
from app.infrastructure.repositories.sqlalchemy.post import SqlAlchemyPostRepository


def get_post_service(
    repo: SqlAlchemyPostRepository = Depends(get_post_repository),
) -> PostService:
    """
    Dependency to provide a PostService with a repository.
    """
    return PostService(repo)
