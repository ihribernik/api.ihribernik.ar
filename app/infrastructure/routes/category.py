from __future__ import annotations

from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from app.application.use_cases.category import CreateCategory
from app.application.use_cases.category import DeleteCategory
from app.application.use_cases.category import GetCategoryById
from app.application.use_cases.category import ListCategories
from app.application.use_cases.category import UpdateCategory
from app.infrastructure.auth.dependencies import get_current_user
from app.schemas.category import CategoryDTO
from app.schemas.category import CreateCategoryDTO

router = APIRouter(
    prefix='/category',
    tags=['blog'],
    dependencies=[Depends(get_current_user)],
)


@router.get('/', response_model=list[CategoryDTO])
async def get_all(use_case: ListCategories = Depends()) -> list[CategoryDTO]:
    categories = use_case.execute()
    return [CategoryDTO(id=c.id, name=c.name, slug=c.slug) for c in categories]


@router.get('/{category_id}', response_model=CategoryDTO)
async def get(category_id: int, use_case: GetCategoryById = Depends()) -> CategoryDTO:
    category = use_case.execute(category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Category not found',
        )

    category_dto = CategoryDTO(
        id=category.id,
        name=category.name,
        slug=category.slug,
        description=category.description,
    )
    return category_dto


@router.post('/', response_model=CategoryDTO, status_code=status.HTTP_201_CREATED)
async def post(
    data: CreateCategoryDTO, use_case: CreateCategory = Depends(),
) -> CategoryDTO:
    category = use_case.execute(data.name, data.slug, data.description)
    return CategoryDTO(
        id=category.id,
        name=category.name,
        slug=category.slug,
        description=category.description,
    )


@router.delete('/{category_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(category_id: int, use_case: DeleteCategory = Depends()) -> None:
    use_case.execute(category_id)
    return None


@router.put(
    '/{category_id}',
    response_model=CategoryDTO,
    status_code=status.HTTP_200_OK,
)
async def update(category_id: int, use_case: UpdateCategory = Depends()) -> CategoryDTO:
    category = use_case.execute(category_id)
    return CategoryDTO(
        id=category.id,
        name=category.name,
        slug=category.slug,
        description=category.description,
    )
