from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Post:
    """
    Domain model for a blog post.
    """

    title: str
    content: str
    author: str
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self) -> None:
        """
        Initialize timestamps if not provided.
        """
        if self.created_at is None:
            self.created_at = datetime.utcnow()
        if self.updated_at is None:
            self.updated_at = self.created_at
