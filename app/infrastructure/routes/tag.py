from __future__ import annotations

from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from app.application.use_cases.tag import CreateTag
from app.application.use_cases.tag import DeleteTag
from app.application.use_cases.tag import GetTagById
from app.application.use_cases.tag import ListTags
from app.application.use_cases.tag import UpdateTag
from app.infrastructure.auth.dependencies import get_current_user
from app.schemas.tag import CreateTagDTO
from app.schemas.tag import TagDTO

router = APIRouter(
    prefix='/tag',
    tags=['blog'],
    dependencies=[Depends(get_current_user)],
)


@router.get('/', response_model=list[TagDTO])
async def get_all(use_case: ListTags = Depends()) -> list[TagDTO]:
    tags = use_case.execute()
    return [TagDTO(id=t.id, name=t.name, slug=t.slug) for t in tags]


@router.get('/{tag_id}', response_model=TagDTO)
async def get(tag_id: int, use_case: GetTagById = Depends()) -> TagDTO:
    tag = use_case.execute(tag_id)
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Tag not found',
        )
    tag_dto = TagDTO(
        id=tag.id,
        name=tag.name,
        slug=tag.slug,
    )
    return tag_dto


@router.post('/', response_model=TagDTO, status_code=status.HTTP_201_CREATED)
async def post(data: CreateTagDTO, use_case: CreateTag = Depends()) -> TagDTO:
    tag = use_case.execute(data.name, data.slug)
    return TagDTO(
        id=tag.id,
        name=tag.name,
        slug=tag.slug,
    )


@router.delete('/{tag_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(tag_id: int, use_case: DeleteTag = Depends()) -> None:
    use_case.execute(tag_id)
    return None


@router.put('/{tag_id}', response_model=TagDTO, status_code=status.HTTP_200_OK)
async def update(tag_id: int, use_case: UpdateTag = Depends()) -> TagDTO:
    tag = use_case.execute(tag_id)
    return TagDTO(
        id=tag.id,
        name=tag.name,
        slug=tag.slug,
    )
