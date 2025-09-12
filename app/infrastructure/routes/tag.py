from __future__ import annotations


from fastapi import APIRouter
from fastapi import Depends

from app.infrastructure.auth.dependencies import get_current_user

router = APIRouter(
    prefix='/tag',
    tags=['blog'],
    dependencies=[Depends(get_current_user)],
)
