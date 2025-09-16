from typing import Optional

from pydantic import BaseModel


class CategoryRequest(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None


class CategoryResponse(BaseModel):
    id: Optional[int]
    name: str
    slug: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
