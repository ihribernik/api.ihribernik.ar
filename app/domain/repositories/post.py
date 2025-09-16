from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.models.post import PostModel


class PostRepository(ABC):
    @abstractmethod
    def get_by_id(self, post_id: int) -> Optional[PostModel]: ...

    @abstractmethod
    def get_by_slug(self, slug: str) -> Optional[PostModel]: ...

    @abstractmethod
    def get_all(self) -> List[PostModel]: ...

    @abstractmethod
    def save(self, post: PostModel) -> PostModel: ...

    @abstractmethod
    def delete(self, post_id: int) -> None: ...
