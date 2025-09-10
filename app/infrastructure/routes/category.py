from typing import List

from fastapi import APIRouter, Depends, status

from app.schemas.category import CategoryDTO

router = APIRouter(prefix="/categories", tags=["blog"])


@router.get("/", response_model=List[CategoryDTO])
async def list() -> List[CategoryDTO]:
    return []


@router.get("/{category_id}", response_model=CategoryDTO)
async def get() -> CategoryDTO:
    return {}


@router.post("/", response_model=CategoryDTO, status_code=status.HTTP_201_CREATED)
async def post() -> CategoryDTO:
    return {}


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete() -> CategoryDTO:
    return {}


@router.put(
    "/{category_id}", response_model=CategoryDTO, status_code=status.HTTP_200_OK
)
async def update() -> CategoryDTO:
    return {}
