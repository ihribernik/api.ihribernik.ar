from fastapi import Depends

from app.application.services.auth import LoginUser
from app.domain.repositories.user import UserRepository
from app.infrastructure.dependencies.respository import get_user_repository


def get_login_user_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> LoginUser:
    """
    Dependency to provide a LoginUserService with a repository.
    """
    return LoginUser(user_repository)
