from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Post:
    id: Optional[int]
    title: str
    content: str
    author: str
    created_at: datetime = datetime.utcnow()
