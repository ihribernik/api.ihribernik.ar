from typing import List

from fastapi import APIRouter, Depends, status

from app.schemas.category import CategorySchema

router = APIRouter(prefix="/categories", tags=["blog"])


@router.get("/", response_model=List[CategorySchema])
async def list() -> List[CategorySchema]:
    return []


@router.get("/{category_id}", response_model=CategorySchema)
async def get() -> CategorySchema:
    return {}


@router.post("/", response_model=CategorySchema, status_code=status.HTTP_201_CREATED)
async def post() -> CategorySchema:
    return {}


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete() -> CategorySchema:
    return {}


@router.put(
    "/{category_id}", response_model=CategorySchema, status_code=status.HTTP_200_OK
)
async def update() -> CategorySchema:
    return {}
