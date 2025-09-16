from __future__ import annotations

from app.domain.models.user import UserModel
from app.infrastructure.database.models import User as UserORM


class UserMapper:
    @staticmethod
    def to_domain(orm: UserORM) -> UserModel:
        return UserModel(
            id=orm.id,
            username=orm.username,
            hashed_password=orm.hashed_password,
        )

    @staticmethod
    def to_orm(entity: UserModel) -> UserORM:
        return UserORM(
            id=entity.id,
            username=entity.username,
            hashed_password=entity.hashed_password,
        )
