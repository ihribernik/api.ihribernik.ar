from __future__ import annotations

from typing import Generic
from typing import List
from typing import Optional
from typing import Protocol
from typing import TypeVar

E = TypeVar('E', contravariant=True)
R = TypeVar('R')
ID = TypeVar('ID', contravariant=True)


class BaseRepository(Protocol, Generic[E, R, ID]):
    """
    Base repository interface.
    """

    def get_by_id(self, entity_id: ID) -> R | None: ...
    def get_by_slug(self, slug: str) -> R | None: ...
    def get_all(self) -> list[R]: ...
    def save(self, entity: E) -> R: ...
    def delete(self, entity_id: ID) -> None: ...
