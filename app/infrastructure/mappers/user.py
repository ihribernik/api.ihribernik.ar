from __future__ import annotations

from app.domain.models.category import Category
from app.domain.models.user import User
from app.infrastructure.database.models import Category as CategoryORM
from app.infrastructure.database.models import User as UserORM


class UserMapper:
    @staticmethod
    def to_domain(orm: UserORM) -> User:
        return User(
            id=orm.id,
            username=orm.username,
            hashed_password=orm.hashed_password,
        )

    @staticmethod
    def to_orm(entity: User) -> UserORM:
        return UserORM(
            id=entity.id,
            username=entity.username,
            hashed_password=entity.hashed_password,
        )


class CategoryMapper:
    @staticmethod
    def to_domain(orm: CategoryORM) -> Category:
        return Category(
            id=orm.id,
            name=orm.name,
            slug=orm.slug,
            description=orm.description,
        )

    @staticmethod
    def to_orm(entity: Category) -> CategoryORM:
        return CategoryORM(
            id=entity.id,
            name=entity.name,
            description=entity.description,
        )
