import re
import unicodedata
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from app.domain.models.tag import Tag
from app.infrastructure.database.models import Category


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", value)


@dataclass
class Post:
    id: Optional[int]
    title: str
    content: str
    category: Optional[Category] = None
    tags: List[Tag] = field(default_factory=list)
    slug: str = field(init=False)
    status: str = "draft"
    published_at: Optional[datetime] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self) -> None:
        self.slug = slugify(self.title)

    def publish(self) -> None:
        self.status = "published"
        self.published_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def add_tag(self, tag: Tag) -> None:
        if tag not in self.tags:
            self.tags.append(tag)
            self.updated_at = datetime.utcnow()

    def change_category(self, category: Category) -> None:
        self.category = category
        self.updated_at = datetime.utcnow()
