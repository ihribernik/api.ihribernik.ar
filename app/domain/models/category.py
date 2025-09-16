from dataclasses import dataclass
from typing import Optional


@dataclass
class CategoryModel:
    id: Optional[int]
    name: str
    slug: str
    description: Optional[str] = None
