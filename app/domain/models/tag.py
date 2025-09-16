from dataclasses import dataclass
from typing import Optional


@dataclass
class TagModel:
    id: Optional[int]
    name: str
    slug: str
