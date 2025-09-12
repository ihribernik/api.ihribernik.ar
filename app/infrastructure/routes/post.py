from __future__ import annotations

from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from app.application.blog_service import BlogService
from app.application.mappers import domain_post_to_schema
from app.application.mappers import schema_to_domain_post
from app.infrastructure.auth.dependencies import get_current_user
from app.infrastructure.database import get_db
from app.infrastructure.repositories.sqlalchemy.post import (
    SqlAlchemyPostRepository,
)
from app.schemas.post import PostDTO

router = APIRouter(
    prefix='/post',
    tags=['blog'],
    dependencies=[Depends(get_current_user)],
)


def get_repo(db: Session = Depends(get_db)) -> SqlAlchemyPostRepository:
    """
    Dependency to provide a SQLAlchemyPostRepository with a session.
    """
    return SqlAlchemyPostRepository(db)


def get_service(repo: SqlAlchemyPostRepository = Depends(get_repo)) -> BlogService:
    """
    Dependency to provide a BlogService with a repository.
    """
    return BlogService(repo)


@router.post('/', response_model=PostDTO, status_code=status.HTTP_201_CREATED)
async def create_post(
    body: PostDTO, service: BlogService = Depends(get_service),
) -> PostDTO:
    """
    Create a new post from the request body.
    :param body: PostDTO from request
    :param service: BlogService dependency
    :return: Created PostDTO
    """
    domain_post = schema_to_domain_post(body)
    created = service.create_post(
        domain_post.title,
        domain_post.content,
    )
    return domain_post_to_schema(created)


@router.get('/', response_model=list[PostDTO])
async def list_posts(service: BlogService = Depends(get_service)) -> list[PostDTO]:
    """
    List all posts.
    :param service: BlogService dependency
    :return: List of PostDTO
    """
    posts = service.list_posts()
    return [domain_post_to_schema(p) for p in posts]
