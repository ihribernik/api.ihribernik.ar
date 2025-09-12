from __future__ import annotations

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer

from app.domain.models.user import User
from app.infrastructure.auth import JWTService
from app.infrastructure.repositories.sqlalchemy.user import (
    SqlAlchemyUserRepository,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    payload = JWTService.verify_token(token, expected_type='access')
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid or expired token',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    username: str = payload.get('sub')
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid token payload',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    repo = SqlAlchemyUserRepository()
    user = repo.get_by_username(username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User not found',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    return user
