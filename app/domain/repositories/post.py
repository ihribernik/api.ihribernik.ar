# app/domain/repositories/post_repository.py
from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.post import Post


class PostRepository(ABC):
    @abstractmethod
    def get_by_id(self, post_id: int) -> Optional[Post]: ...

    @abstractmethod
    def get_by_slug(self, slug: str) -> Optional[Post]: ...

    @abstractmethod
    def list(self) -> List[Post]: ...

    @abstractmethod
    def save(self, post: Post) -> Post: ...

    @abstractmethod
    def delete(self, post_id: int) -> None: ...
