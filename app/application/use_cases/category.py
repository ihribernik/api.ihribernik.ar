from __future__ import annotations

from typing import List
from typing import Optional

from app.domain.models.category import Category
from app.domain.repositories.category import CategoryRepository


class CreateCategory:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self, name: str, slug: str, description: str | None = None) -> Category:
        category = Category(id=None, name=name, slug=slug, description=description)
        return self.repo.save(category)


class GetCategoryBySlug:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self, slug: str) -> Category | None:
        return self.repo.get_by_slug(slug)


class ListCategories:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self) -> list[Category]:
        return self.repo.list()


class GetCategoryById:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self, category_id: int) -> Category | None:
        return self.repo.get_by_id(category_id)


class UpdateCategory:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self, category_id: int) -> Category | None:
        return self.repo.get_by_id(category_id)


class DeleteCategory:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self, category_id: int) -> None:
        self.repo.delete(category_id)
