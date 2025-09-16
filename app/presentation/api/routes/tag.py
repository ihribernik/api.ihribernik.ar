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
from app.presentation.schemas.tag import TagRequest, TagResponse

router = APIRouter(
    prefix="/tag",
    tags=["blog"],
    dependencies=[Depends(get_current_user)],
)


@router.get("/", response_model=list[TagResponse])
async def get_all(use_case: ListTags = Depends()) -> list[TagResponse]:
    tags = use_case.execute()
    return [TagResponse(id=t.id, name=t.name, slug=t.slug) for t in tags]


@router.get("/{tag_id}", response_model=TagResponse)
async def get(tag_id: int, use_case: GetTagById = Depends()) -> TagResponse:
    tag = use_case.execute(tag_id)
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
async def post(data: TagRequest, use_case: CreateTag = Depends()) -> TagResponse:
    tag = use_case.execute(data.name, data.slug)
    return TagResponse(
        id=tag.id,
        name=tag.name,
        slug=tag.slug,
    )


@router.delete("/{tag_id}")
async def delete(tag_id: int, use_case: DeleteTag = Depends()) -> None:
    use_case.execute(tag_id)
    return None


@router.put("/{tag_id}", response_model=TagResponse, status_code=status.HTTP_200_OK)
async def update(tag_id: int, use_case: UpdateTag = Depends()) -> TagResponse:
    tag = use_case.execute(tag_id)
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
