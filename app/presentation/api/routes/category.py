from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from app.application.services.category import CreateCategory
from app.application.services.category import DeleteCategory
from app.application.services.category import GetCategoryById
from app.application.services.category import ListCategories
from app.application.services.category import UpdateCategory
from app.infrastructure.dependencies.auth import get_current_user
from app.presentation.schemas.category import CategoryRequest
from app.presentation.schemas.category import CategoryResponse

router = APIRouter(
    prefix='/category',
    tags=['blog'],
    dependencies=[Depends(get_current_user)],
)


@router.get('/', response_model=list[CategoryResponse])
async def get_all(use_case: ListCategories = Depends()) -> list[CategoryResponse]:
    categories = use_case.execute()
    return [CategoryResponse(id=c.id, name=c.name, slug=c.slug) for c in categories]


@router.get('/{category_id}', response_model=CategoryResponse)
async def get(
    category_id: int,
    use_case: GetCategoryById = Depends(),
) -> CategoryResponse:
    category = use_case.execute(category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Category not found',
        )

    category_dto = CategoryResponse(
        id=category.id,
        name=category.name,
        slug=category.slug,
        description=category.description,
    )
    return category_dto


@router.post('/', response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def post(
    data: CategoryRequest,
    use_case: CreateCategory = Depends(),
) -> CategoryResponse:
    category = use_case.execute(data.name, data.slug, data.description)
    return CategoryResponse(
        id=category.id,
        name=category.name,
        slug=category.slug,
        description=category.description,
    )


@router.delete('/{category_id}')
async def delete(category_id: int, use_case: DeleteCategory = Depends()) -> None:
    use_case.execute(category_id)
    return None


@router.put(
    '/{category_id}',
    response_model=CategoryResponse,
    status_code=status.HTTP_200_OK,
)
async def update(
    category_id: int,
    use_case: UpdateCategory = Depends(),
) -> CategoryResponse:
    category = use_case.execute(category_id)

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Category not found',
        )

    return CategoryResponse(
        id=category.id,
        name=category.name,
        slug=category.slug,
        description=category.description,
    )
