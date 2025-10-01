from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from app.application.services.auth import LoginUser
from app.infrastructure.auth import JWTService
from app.infrastructure.dependencies.service.auth import get_login_user_service
from app.presentation.schemas.auth import LoginRequest
from app.presentation.schemas.auth import RefreshRequest
from app.presentation.schemas.auth import TokenPairResponse

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/login', response_model=TokenPairResponse)
def login(
    data: LoginRequest,
    service: LoginUser = Depends(get_login_user_service),
) -> TokenPairResponse:
    token = service.execute(data.username, data.password)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid credentials',
        )

    refresh_token = JWTService.create_refresh_token({'sub': data.username})

    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Error creating refresh token',
        )

    return TokenPairResponse(access_token=token, refresh_token=refresh_token)


@router.post('/refresh', response_model=dict)
def refresh(data: RefreshRequest) -> dict[str, str]:
    new_access_token = JWTService.refresh_access_token(data.refresh_token)
    if not new_access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid refresh token',
        )

    return {'access_token': new_access_token, 'token_type': 'bearer'}
