# app/infrastructure/repositories/sqlalchemy_tag_repository.py
from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.models.tag import Tag
from app.domain.repositories.tag import TagRepository
from app.infrastructure.database.models import Tag as TagORM


class SqlAlchemyTagRepository(TagRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, tag_id: int) -> Optional[Tag]:
        orm = self.session.get(TagORM, tag_id)
        return self._to_domain(orm) if orm else None

    def get_by_slug(self, slug: str) -> Optional[Tag]:
        orm = self.session.query(TagORM).filter_by(slug=slug).first()
        return self._to_domain(orm) if orm else None

    def list(self) -> List[Tag]:
        return [self._to_domain(o) for o in self.session.query(TagORM).all()]

    def save(self, tag: Tag) -> Tag:
        if tag.id:
            orm = self.session.get(TagORM, tag.id)
            if orm:
                orm.name = tag.name
                orm.slug = tag.slug
        else:
            orm = TagORM(name=tag.name, slug=tag.slug)
            self.session.add(orm)

        self.session.commit()
        return self._to_domain(orm)

    def delete(self, tag_id: int) -> None:
        orm = self.session.get(TagORM, tag_id)
        if orm:
            self.session.delete(orm)
            self.session.commit()

    def _to_domain(self, orm: TagORM) -> Tag:
        return Tag(
            id=orm.id,
            name=orm.name,
            slug=orm.slug,
        )
