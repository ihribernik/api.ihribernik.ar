from __future__ import annotations

from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from app.infrastructure.auth.dependencies import get_current_user
from app.schemas.category import CategoryDTO

router = APIRouter(
    prefix='/category',
    tags=['blog'],
    dependencies=[Depends(get_current_user)],
)


@router.get('/', response_model=list[CategoryDTO])
async def list() -> list[CategoryDTO]:
    return []


@router.get('/{category_id}', response_model=CategoryDTO)
async def get() -> CategoryDTO:
    return {}


@router.post('/', response_model=CategoryDTO, status_code=status.HTTP_201_CREATED)
async def post() -> CategoryDTO:
    return {}


@router.delete('/{category_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete() -> None:
    return None


@router.put(
    '/{category_id}', response_model=CategoryDTO, status_code=status.HTTP_200_OK,
)
async def update() -> CategoryDTO:
    return {}
