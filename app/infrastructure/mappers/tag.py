from __future__ import annotations

from app.domain.models.tag import TagModel
from app.infrastructure.database.models import Tag as TagORM
from app.presentation.schemas.tag import TagResponse


class TagMapper:
    @staticmethod
    def to_domain(orm: TagORM | None) -> TagModel:

        if orm is None:
            raise ValueError('ORM object cannot be None')

        return TagModel(
            id=orm.id,
            name=orm.name,
            slug=orm.slug,
        )

    @staticmethod
    def to_orm(entity: TagModel) -> TagORM:
        return TagORM(
            id=entity.id,
            name=entity.name,
            slug=entity.slug,
        )

    @staticmethod
    def to_dto(entity: TagModel) -> TagResponse:
        return TagResponse(
            id=entity.id,
            name=entity.name,
            slug=entity.slug,
        )
