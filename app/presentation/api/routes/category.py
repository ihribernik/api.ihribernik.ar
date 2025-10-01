from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from app.application.services import Service
from app.infrastructure.dependencies.auth import get_current_user
from app.infrastructure.dependencies.service.category import (
    get_create_category_service,
    get_delete_category_service,
    get_get_category_by_id_service,
    get_get_category_by_slug_service,
    get_list_category_service,
    get_update_category_service,
)
from app.presentation.schemas.category import CategoryRequest, CategoryResponse

router = APIRouter(
    prefix="/category",
    tags=["Category"],
    dependencies=[Depends(get_current_user)],
)


@router.get("/", response_model=list[CategoryResponse])
async def get_all(
    service: Service = Depends(get_list_category_service),
) -> list[CategoryResponse]:
    categories = service.execute()
    return [CategoryResponse(id=c.id, name=c.name, slug=c.slug) for c in categories]


@router.get("/{category_id}", response_model=CategoryResponse)
async def get(
    category_id: int,
    service: Service = Depends(get_get_category_by_id_service),
) -> CategoryResponse:
    category = service.execute(category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    category_dto = CategoryResponse(
        id=category.id,
        name=category.name,
        slug=category.slug,
        description=category.description,
    )
    return category_dto


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def post(
    data: CategoryRequest,
    service: Service = Depends(get_create_category_service),
) -> CategoryResponse:
    category = service.execute(data.name, data.slug, data.description)
    return CategoryResponse(
        id=category.id,
        name=category.name,
        slug=category.slug,
        description=category.description,
    )


@router.delete("/{category_id}")
async def delete(
    category_id: int, service: Service = Depends(get_delete_category_service)
) -> None:
    service.execute(category_id)
    return None


@router.put(
    "/{category_id}",
    response_model=CategoryResponse,
    status_code=status.HTTP_200_OK,
)
async def update(
    category_id: int,
    service: Service = Depends(get_update_category_service),
) -> CategoryResponse:
    category = service.execute(category_id)

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return CategoryResponse(
        id=category.id,
        name=category.name,
        slug=category.slug,
        description=category.description,
    )
