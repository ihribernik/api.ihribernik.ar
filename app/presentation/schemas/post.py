from typing import List, Optional

from pydantic import BaseModel

from app.presentation.schemas.category import CategoryResponse
from app.presentation.schemas.tag import TagResponse


class PostRequest(BaseModel):
    title: str
    content: str


class PostResponse(BaseModel):
    id: Optional[int]
    title: str
    content: str
    slug: str
    category: Optional[CategoryResponse] = None
    tags: List[TagResponse] = []

    class Config:
        orm_mode = True
