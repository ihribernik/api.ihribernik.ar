from __future__ import annotations

from app.domain.models.post import PostModel
from app.infrastructure.database.models import Post as PostORM
from app.infrastructure.mappers.category import CategoryMapper
from app.infrastructure.mappers.tag import TagMapper
from app.presentation.schemas.post import PostResponse


class PostMapper:
    @staticmethod
    def to_domain(orm: PostORM) -> PostModel:
        return PostModel(
            id=orm.id,
            title=orm.title,
            content=orm.content,
        )

    @staticmethod
    def to_orm(entity: PostModel) -> PostORM:
        return PostORM(
            id=entity.id,
            title=entity.title,
            content=entity.content,
            slug=entity.slug,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    @staticmethod
    def to_dto(entity: PostModel) -> PostResponse:
        return PostResponse(
            id=entity.id,
            title=entity.title,
            content=entity.content,
            slug=entity.slug,
            category=CategoryMapper.to_dto(entity.category),
            tags=[TagMapper.to_dto(t) for t in entity.tags],
        )
