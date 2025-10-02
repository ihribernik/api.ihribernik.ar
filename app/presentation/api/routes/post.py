from __future__ import annotations

from fastapi import APIRouter, Depends, status

from app.application.services import Service
from app.infrastructure.dependencies.auth import get_current_user
from app.infrastructure.dependencies.service.post import (
    get_create_post_service,
    get_delete_post_service,
    get_get_post_by_id_service,
    get_get_post_by_slug_service,
    get_list_post_service,
    get_update_post_service,
)
from app.infrastructure.mappers.post import PostMapper
from app.presentation.schemas.post import PostRequest, PostResponse

router = APIRouter(
    prefix="/post",
    tags=["Post"],
    dependencies=[Depends(get_current_user)],
)


@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(
    body: PostRequest,
    service: Service = Depends(get_create_post_service),
) -> PostResponse:
    """
    Create a new post from the request body.
        :param body: PostRequest from request
        :param service: PostService dependency

    :return: Created PostResponse
    """
    created = service.execute(
        body.title,
        body.content,
    )
    return PostMapper.to_dto(created)


@router.get("/", response_model=list[PostResponse])
async def list_posts(
    service: Service = Depends(get_list_post_service),
) -> list[PostResponse]:
    """
    List all posts.
    :param service: PostService dependency
    :return: List of PostResponse
    """
    posts = service.execute()
    return [PostMapper.to_dto(p) for p in posts]


@router.get("/{post_id}", response_model=PostResponse)
async def get_post(
    post_id: int,
    service: Service = Depends(get_get_post_by_id_service),
) -> PostResponse:
    """
    Get a post by its ID.
    :param post_id: ID of the post
    :param service: PostService dependency
    :return: PostResponse
    """
    post = service.execute(post_id)
    return PostMapper.to_dto(post)


@router.get("/slug/{slug}", response_model=PostResponse)
async def get_post_by_slug(
    slug: str,
    service: Service = Depends(get_get_post_by_slug_service),
) -> PostResponse:
    """
    Get a post by its slug.
    :param slug: Slug of the post
    :param service: PostService dependency
    :return: PostResponse
    """
    post = service.execute(slug)
    return PostMapper.to_dto(post)


@router.put(
    "/{post_id}",
    response_model=PostResponse,
    status_code=status.HTTP_200_OK,
)
async def update_post(
    post_id: int,
    service: Service = Depends(get_update_post_service),
) -> PostResponse:
    """
    Update a post by its ID.
    :param post_id: ID of the post
    :param service: PostService dependency
    :return: PostResponse
    """
    post = service.execute(post_id)
    return PostMapper.to_dto(post)


@router.delete("/{post_id}")
async def delete_post(
    post_id: int, service: Service = Depends(get_delete_post_service)
) -> None:
    """
    Delete a post by its ID.
    :param post_id: ID of the post
    :param service: PostService dependency
    :return: None
    """
    service.execute(post_id)
    return None
