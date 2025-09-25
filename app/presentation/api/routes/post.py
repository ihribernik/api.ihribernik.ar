from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from app.application.services.post import PostService
from app.infrastructure.dependencies.auth import get_current_user
from app.infrastructure.dependencies.service import get_post_service
from app.infrastructure.mappers.post import PostMapper
from app.presentation.schemas.post import PostRequest
from app.presentation.schemas.post import PostResponse

router = APIRouter(
    prefix='/post',
    tags=['blog'],
    dependencies=[Depends(get_current_user)],
)


@router.post('/', response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(
    body: PostRequest,
    service: PostService = Depends(get_post_service),
) -> PostResponse:
    """
    Create a new post from the request body.
    :param body: PostRequest from request
    :param service: PostService dependency
    :return: Created PostResponse
    """
    created = service.create(
        body.title,
        body.content,
    )
    return PostMapper.to_dto(created)


@router.get('/', response_model=list[PostResponse])
async def list_posts(
    service: PostService = Depends(get_post_service),
) -> list[PostResponse]:
    """
    List all posts.
    :param service: PostService dependency
    :return: List of PostResponse
    """
    posts = service.get_all()
    return [PostMapper.to_dto(p) for p in posts]
