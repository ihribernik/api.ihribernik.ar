from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from app.application.services.tag import (
    CreateTag,
    DeleteTag,
    GetTagById,
    ListTags,
    UpdateTag,
)
from app.infrastructure.dependencies.auth import get_current_user
from app.infrastructure.dependencies.service.tag import (
    get_create_tag_service,
    get_delete_tag_service,
    get_get_tag_by_id_service,
    get_get_tag_by_slug_service,
    get_list_tag_service,
    get_update_tag_service,
)
from app.presentation.schemas.tag import TagRequest, TagResponse

router = APIRouter(
    prefix="/tag",
    tags=["Tag"],
    dependencies=[Depends(get_current_user)],
)


@router.get("/", response_model=list[TagResponse])
async def get_all(
    service: ListTags = Depends(get_list_tag_service),
) -> list[TagResponse]:
    tags = service.execute()
    return [TagResponse(id=t.id, name=t.name, slug=t.slug) for t in tags]


@router.get("/{tag_id}", response_model=TagResponse)
async def get(
    tag_id: int, service: GetTagById = Depends(get_get_tag_by_id_service)
) -> TagResponse:
    tag = service.execute(tag_id)
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tag not found",
        )
    tag_dto = TagResponse(
        id=tag.id,
        name=tag.name,
        slug=tag.slug,
    )
    return tag_dto


@router.post("/", response_model=TagResponse, status_code=status.HTTP_201_CREATED)
async def post(
    data: TagRequest, service: CreateTag = Depends(get_create_tag_service)
) -> TagResponse:
    tag = service.execute(data.name, data.slug)
    return TagResponse(
        id=tag.id,
        name=tag.name,
        slug=tag.slug,
    )


@router.delete("/{tag_id}")
async def delete(
    tag_id: int, service: DeleteTag = Depends(get_delete_tag_service)
) -> None:
    service.execute(tag_id)
    return None


@router.put("/{tag_id}", response_model=TagResponse, status_code=status.HTTP_200_OK)
async def update(
    tag_id: int, service: UpdateTag = Depends(get_update_tag_service)
) -> TagResponse:
    tag = service.execute(tag_id)
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tag not found",
        )

    return TagResponse(
        id=tag.id,
        name=tag.name,
        slug=tag.slug,
    )
