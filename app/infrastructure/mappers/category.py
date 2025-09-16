from typing import Optional

from app.domain.models.category import CategoryModel
from app.infrastructure.database.models import Category as CategoryORM
from app.presentation.schemas.category import CategoryResponse


class CategoryMapper:
    @staticmethod
    def to_domain(orm: CategoryORM) -> CategoryModel:
        return CategoryModel(
            id=orm.id,
            name=orm.name,
            slug=orm.slug,
            description=orm.description,
        )

    @staticmethod
    def to_orm(entity: CategoryModel) -> CategoryORM:
        return CategoryORM(
            id=entity.id,
            name=entity.name,
            description=entity.description,
        )

    @staticmethod
    def to_dto(entity: Optional[CategoryModel]) -> Optional[CategoryResponse]:
        if entity is None:
            return None

        return CategoryResponse(
            id=entity.id,
            name=entity.name,
            slug=entity.slug,
            description=entity.description,
        )
