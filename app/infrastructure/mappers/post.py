from __future__ import annotations

from app.domain.models.post import Post
from app.infrastructure.database.models import Post as PostORM


class PostMapper:
    @staticmethod
    def to_domain(orm: PostORM) -> Post:
        return Post(
            id=orm.id,
            title=orm.title,
            content=orm.content,
        )

    @staticmethod
    def to_orm(entity: Post) -> PostORM:
        return PostORM(
            id=entity.id,
            title=entity.title,
            content=entity.content,
            slug=entity.slug,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
