from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.models.tag import TagModel
from app.domain.repositories.tag import TagRepository
from app.infrastructure.database.models import Tag as TagORM
from app.infrastructure.mappers.tag import TagMapper


class SqlAlchemyTagRepository(TagRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, tag_id: int) -> Optional[TagModel]:
        orm = self.session.get(TagORM, tag_id)
        return TagMapper.to_domain(orm) if orm else None

    def get_by_slug(self, slug: str) -> Optional[TagModel]:
        orm = self.session.query(TagORM).filter_by(slug=slug).first()
        return TagMapper.to_domain(orm) if orm else None

    def get_all(self) -> List[TagModel]:
        tags = self.session.query(TagORM).all()
        return [TagMapper.to_domain(o) for o in tags]

    def save(self, tag: TagModel) -> TagModel:
        if tag.id:
            orm = self.session.get(TagORM, tag.id)
            if orm:
                orm.name = tag.name
                orm.slug = tag.slug
        else:
            orm = TagORM(name=tag.name, slug=tag.slug)
            self.session.add(orm)

        self.session.commit()
        return TagMapper.to_domain(orm)

    def delete(self, tag_id: int) -> None:
        orm = self.session.get(TagORM, tag_id)
        if orm:
            self.session.delete(orm)
            self.session.commit()

    def _to_domain(self, orm: TagORM) -> TagModel:
        return TagModel(
            id=orm.id,
            name=orm.name,
            slug=orm.slug,
        )
