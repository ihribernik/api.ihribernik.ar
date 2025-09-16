from __future__ import annotations

from app.domain.models.category import CategoryModel
from app.domain.repositories.category import CategoryRepository


class CreateCategory:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(
        self, name: str, slug: str, description: str | None = None
    ) -> CategoryModel:
        category = CategoryModel(id=None, name=name, slug=slug, description=description)
        return self.repo.save(category)


class GetCategoryBySlug:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self, slug: str) -> CategoryModel | None:
        return self.repo.get_by_slug(slug)


class ListCategories:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self) -> list[CategoryModel]:
        return self.repo.get_all()


class GetCategoryById:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self, category_id: int) -> CategoryModel | None:
        return self.repo.get_by_id(category_id)


class UpdateCategory:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self, category_id: int) -> CategoryModel | None:
        return self.repo.get_by_id(category_id)


class DeleteCategory:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self, category_id: int) -> None:
        self.repo.delete(category_id)
