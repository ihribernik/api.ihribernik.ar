from __future__ import annotations

from sqlalchemy.orm import Session

from app.domain.models.user import User
from app.domain.repositories.user import UserRepository
from app.infrastructure.database.models import User as UserORM
from app.infrastructure.database.session import get_session  # TODO - Revisar


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session | None = None):
        self.session = session or get_session()

    def get_by_username(self, username: str) -> User | None:
        user_orm = (
            self.session.query(UserORM).filter(UserORM.username == username).first()
        )
        if not user_orm:
            return None
        return User(
            id=user_orm.id,
            username=user_orm.username,
            hashed_password=user_orm.hashed_password,
        )

    def save(self, user: User) -> User:
        if user.id:
            user_orm = self.session.get(UserORM, user.id)
            if not user_orm:
                raise ValueError("User not found")
            user_orm.username = user.username
            user_orm.hashed_password = user.hashed_password
        else:
            user_orm = UserORM(
                username=user.username, hashed_password=user.hashed_password
            )
            self.session.add(user_orm)

        self.session.commit()
        self.session.refresh(user_orm)
        return User(
            id=user_orm.id,
            username=user_orm.username,
            hashed_password=user_orm.hashed_password,
        )
