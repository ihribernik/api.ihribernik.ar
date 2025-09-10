# app/application/use_cases/category_use_cases.py
from typing import List, Optional

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

    def execute(self, slug: str) -> Optional[Category]:
        return self.repo.get_by_slug(slug)

class ListCategories:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self) -> List[Category]:
        return self.repo.list()
