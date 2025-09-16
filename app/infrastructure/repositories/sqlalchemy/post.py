# app/infrastructure/repositories/sqlalchemy_post_repository.py
from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.models.category import CategoryModel
from app.domain.models.post import PostModel
from app.domain.models.tag import TagModel
from app.domain.repositories.post import PostRepository
from app.infrastructure.database.models import Category as CategoryORM
from app.infrastructure.database.models import Post as PostORM
from app.infrastructure.database.models import Tag as TagORM
from app.infrastructure.mappers.post import PostMapper


class SqlAlchemyPostRepository(PostRepository):
    """
    SQLAlchemy implementation of the PostRepository interface.
    """

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, post_id: int) -> Optional[PostModel]:
        orm = self.session.get(PostORM, post_id)
        return PostMapper.to_domain(orm) if orm else None

    def get_by_slug(self, slug: str) -> Optional[PostModel]:
        orm = self.session.query(PostORM).filter_by(slug=slug).first()
        return PostMapper.to_domain(orm) if orm else None

    def get_all(self) -> List[PostModel]:
        return [PostMapper.to_domain(o) for o in self.session.query(PostORM).all()]

    def save(self, post: PostModel) -> PostModel:
        if post.id:
            orm = self.session.get(PostORM, post.id)
            if orm:
                orm.title = post.title
                orm.content = post.content
                orm.slug = post.slug
                orm.status = post.status
                orm.updated_at = post.updated_at
        else:
            orm = self._to_orm(post)
            self.session.add(orm)

        self.session.commit()
        return PostMapper.to_domain(orm)

    def delete(self, post_id: int) -> None:
        orm = self.session.get(PostORM, post_id)
        if orm:
            self.session.delete(orm)
            self.session.commit()

    def _to_domain(self, orm: PostORM) -> PostModel:
        category = None
        if orm.category:
            category = CategoryModel(
                id=orm.category.id,
                name=orm.category.name,
                slug=orm.category.slug,
                description=orm.category.description,
            )
        tags = [TagModel(id=t.id, name=t.name, slug=t.slug) for t in orm.tags]
        return PostModel(
            id=orm.id,
            title=orm.title,
            content=orm.content,
            category=category,
            tags=tags,
            status=orm.status,
            published_at=orm.published_at,
            created_at=orm.created_at,
            updated_at=orm.updated_at,
        )

    def _to_orm(self, post: PostModel) -> PostORM:
        orm = PostORM(
            title=post.title,
            content=post.content,
            slug=post.slug,
            status=post.status,
            published_at=post.published_at,
        )
        if post.category:
            orm.category = self.session.get(CategoryORM, post.category.id)

        # TODO - Revisar esto
        orm.tags = [
            tag
            for tag in (self.session.get(TagORM, t.id) for t in post.tags if t.id)
            if tag is not None
        ]
        return orm
