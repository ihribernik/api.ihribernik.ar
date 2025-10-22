from __future__ import annotations

from dataclasses import dataclass

from app.infrastructure.auth import PasswordService


@dataclass
class UserModel:
    id: int | None
    username: str
    hashed_password: str

    def verify_password(self, plain_password: str) -> bool:

        return PasswordService.verify(plain_password, self.hashed_password)
