from typing import List, Optional
from pydantic import BaseModel

from app.schemas.category import CategoryDTO
from app.schemas.tag import TagDTO


class PostDTO(BaseModel):
    id: Optional[int]
    title: str
    content: str
    slug: str
    category: Optional[CategoryDTO] = None
    tags: List[TagDTO] = []

    class Config:
        orm_mode = True


class CreatePostDTO(BaseModel):
    title: str
    content: str
    slug: str
