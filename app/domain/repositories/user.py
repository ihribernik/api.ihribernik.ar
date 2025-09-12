from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Optional

from app.domain.models.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_by_username(self, username: str) -> User | None:
        """Busca un usuario por username"""
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        """Guarda o actualiza un usuario"""
        pass
