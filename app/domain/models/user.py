from __future__ import annotations

import hashlib
from dataclasses import dataclass


@dataclass
class UserModel:
    id: int | None
    username: str
    hashed_password: str

    def verify_password(self, plain_password: str) -> bool:

        return (
            hashlib.sha256(plain_password.encode()).hexdigest() == self.hashed_password
        )
