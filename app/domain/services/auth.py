from __future__ import annotations

from datetime import timedelta

from app.domain.exceptions import UnauthorizedError
from app.domain.models.user import User
from app.infrastructure.auth import JWTService
from app.infrastructure.auth import PasswordService


class AuthService:
    def __init__(self, jwt_service: JWTService, password_service: PasswordService):
        self.jwt_service = jwt_service
        self.password_service = password_service

    def authenticate_user(self, user: User, password: str) -> str:
        if not self.password_service.verify(password, user.hashed_password):
            raise UnauthorizedError('Invalid credentials')

        # Generar JWT
        token_expires = timedelta(minutes=60)
        return self.jwt_service.create_access_token(
            data={'sub': user.email}, expires_delta=token_expires,
        )

    def refresh_token(self, refresh_token: str) -> str:
        return self.jwt_service.refresh_access_token(refresh_token)
