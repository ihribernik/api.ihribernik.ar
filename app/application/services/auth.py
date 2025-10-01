from __future__ import annotations

from datetime import timedelta

from app.application.services import Service
from app.domain.repositories.user import UserRepository
from app.infrastructure.auth import JWTService


class LoginUser(Service):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, username: str, password: str) -> str | None:
        user = self.user_repository.get_by_username(username)
        if not user or not user.verify_password(password):
            return None

        token = JWTService.create_access_token(
            data={"sub": user.username},
            expires_delta=timedelta(minutes=30),
        )
        return token
