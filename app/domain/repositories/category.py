# app/domain/repositories/category_repository.py
from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.category import Category


class CategoryRepository(ABC):
    @abstractmethod
    def get_by_id(self, category_id: int) -> Optional[Category]: ...

    @abstractmethod
    def get_by_slug(self, slug: str) -> Optional[Category]: ...

    @abstractmethod
    def list(self) -> List[Category]: ...

    @abstractmethod
    def save(self, category: Category) -> Category: ...

    @abstractmethod
    def delete(self, category_id: int) -> None: ...
