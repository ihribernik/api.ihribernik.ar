from __future__ import annotations

from typing import Dict

from fastapi import APIRouter, HTTPException, status

from app.application.use_cases.auth import LoginUser
from app.infrastructure.auth import JWTService
from app.infrastructure.repositories.sqlalchemy.user import SqlAlchemyUserRepository
from app.schemas.auth import LoginRequest, RefreshRequest, TokenPairResponse

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=TokenPairResponse)
def login(data: LoginRequest) -> TokenPairResponse:
    repo = SqlAlchemyUserRepository()
    use_case = LoginUser(repo)

    token = use_case.execute(data.username, data.password)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    refresh_token = JWTService.create_refresh_token({"sub": data.username})

    return TokenPairResponse(access_token=token, refresh_token=refresh_token)


@router.post("/refresh", response_model=dict)
def refresh(data: RefreshRequest) -> Dict[str, str]:
    new_access_token = JWTService.refresh_access_token(data.refresh_token)
    if not new_access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    return {"access_token": new_access_token, "token_type": "bearer"}
