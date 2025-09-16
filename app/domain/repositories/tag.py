from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.models.tag import TagModel


class TagRepository(ABC):
    @abstractmethod
    def get_by_id(self, tag_id: int) -> Optional[TagModel]: ...

    @abstractmethod
    def get_by_slug(self, slug: str) -> Optional[TagModel]: ...

    @abstractmethod
    def get_all(self) -> List[TagModel]: ...

    @abstractmethod
    def save(self, tag: TagModel) -> TagModel: ...

    @abstractmethod
    def delete(self, tag_id: int) -> None: ...
