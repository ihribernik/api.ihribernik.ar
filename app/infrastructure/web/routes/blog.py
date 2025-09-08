from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.application.blog_service import BlogService
from app.application.mappers import domain_post_to_schema, schema_to_domain_post
from app.infrastructure.database import get_db
from app.infrastructure.repositories.sqlalchemy_post_repo import (
    SqlAlchemyPostRepository,
)
from app.schemas.post_schema import PostSchema

router = APIRouter(prefix="/posts", tags=["blog"])


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


@router.post("/", response_model=PostSchema, status_code=status.HTTP_201_CREATED)
async def create_post(
    body: PostSchema, service: BlogService = Depends(get_service)
) -> PostSchema:
    """
    Create a new post from the request body.
    :param body: PostSchema from request
    :param service: BlogService dependency
    :return: Created PostSchema
    """
    domain_post = schema_to_domain_post(body)
    created = service.create_post(
        domain_post.title, domain_post.content, domain_post.author
    )
    return domain_post_to_schema(created)


@router.get("/", response_model=List[PostSchema])
async def list_posts(service: BlogService = Depends(get_service)) -> List[PostSchema]:
    """
    List all posts.
    :param service: BlogService dependency
    :return: List of PostSchema
    """
    posts = service.list_posts()
    return [domain_post_to_schema(p) for p in posts]
