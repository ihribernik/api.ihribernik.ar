from typing import Optional

from pydantic import BaseModel


class TagRequest(BaseModel):
    name: str
    slug: str


class TagResponse(BaseModel):
    id: Optional[int]
    name: str
    slug: str

    class Config:
        orm_mode = True
