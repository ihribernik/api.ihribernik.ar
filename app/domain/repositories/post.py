from __future__ import annotations

from app.domain.models.post import PostModel
from app.domain.repositories import BaseRepository


class PostRepository(BaseRepository[PostModel, PostModel, int]):
    pass
