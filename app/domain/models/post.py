from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone

from app.domain.models.category import CategoryModel
from app.domain.models.tag import TagModel


def slugify(value: str) -> str:
    value = unicodedata.normalize('NFKD', value)
    value = value.encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)


@dataclass
class PostModel:
    id: int | None
    title: str
    content: str
    category: CategoryModel | None = None
    tags: list[TagModel] = field(default_factory=list)
    slug: str = field(init=False)
    status: str = 'draft'
    published_at: datetime | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        self.slug = slugify(self.title)

    def publish(self) -> None:
        self.status = 'published'
        self.published_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    def add_tag(self, tag: TagModel) -> None:
        if tag not in self.tags:
            self.tags.append(tag)
            self.updated_at = datetime.now(timezone.utc)

    def change_category(self, category: CategoryModel) -> None:
        self.category = category
        self.updated_at = datetime.now(timezone.utc)
