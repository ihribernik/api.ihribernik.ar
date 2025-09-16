from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.models.category import CategoryModel


class CategoryRepository(ABC):
    @abstractmethod
    def get_by_id(self, category_id: int) -> Optional[CategoryModel]: ...

    @abstractmethod
    def get_by_slug(self, slug: str) -> Optional[CategoryModel]: ...

    @abstractmethod
    def get_all(self) -> List[CategoryModel]: ...

    @abstractmethod
    def save(self, category: CategoryModel) -> CategoryModel: ...

    @abstractmethod
    def delete(self, category_id: int) -> None: ...
