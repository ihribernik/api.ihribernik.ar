from __future__ import annotations

from app.domain.models.category import CategoryModel
from app.domain.repositories import BaseRepository


class CategoryRepository(BaseRepository[CategoryModel, CategoryModel, int]):
    pass
