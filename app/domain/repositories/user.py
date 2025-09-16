from __future__ import annotations

from abc import ABC, abstractmethod

from app.domain.models.user import UserModel


class UserRepository(ABC):
    @abstractmethod
    def get_by_username(self, username: str) -> UserModel | None:
        """Busca un usuario por username"""
        pass

    @abstractmethod
    def save(self, user: UserModel) -> UserModel:
        """Guarda o actualiza un usuario"""
        pass
