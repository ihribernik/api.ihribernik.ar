# app/domain/repositories/tag_repository.py
from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models import Tag


class TagRepository(ABC):
    @abstractmethod
    def get_by_id(self, tag_id: int) -> Optional[Tag]: ...

    @abstractmethod
    def get_by_slug(self, slug: str) -> Optional[Tag]: ...

    @abstractmethod
    def list(self) -> List[Tag]: ...

    @abstractmethod
    def save(self, tag: Tag) -> Tag: ...

    @abstractmethod
    def delete(self, tag_id: int) -> None: ...
