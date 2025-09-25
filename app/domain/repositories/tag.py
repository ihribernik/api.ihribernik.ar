from __future__ import annotations

from app.domain.models.tag import TagModel
from app.domain.repositories import BaseRepository


class TagRepository(BaseRepository[TagModel, TagModel, int]):
    pass
