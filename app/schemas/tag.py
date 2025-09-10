from typing import Optional
from pydantic import BaseModel


class TagDTO(BaseModel):
    id: Optional[int]
    name: str
    slug: str

    class Config:
        orm_mode = True


class CreateTagDTO(BaseModel):
    name: str
    slug: str
