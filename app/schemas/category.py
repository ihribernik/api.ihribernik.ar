from typing import Optional
from pydantic import BaseModel


class CategoryDTO(BaseModel):
    id: Optional[int]
    name: str
    slug: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class CreateCategoryDTO(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None
