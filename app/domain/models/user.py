from __future__ import annotations

from dataclasses import dataclass


@dataclass
class User:
    id: int | None
    username: str
    hashed_password: str

    def verify_password(self, plain_password: str) -> bool:
        # Aquí deberías usar bcrypt/argon2, no comparar en plano
        import hashlib
        return hashlib.sha256(plain_password.encode()).hexdigest() == self.hashed_password
