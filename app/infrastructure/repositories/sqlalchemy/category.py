# app/infrastructure/repositories/sqlalchemy_category_repository.py
from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.models import Category
from app.domain.repositories.category import CategoryRepository
from app.infrastructure.database.models import Category as CategoryORM

class SqlAlchemyCategoryRepository(CategoryRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, category_id: int) -> Optional[Category]:
        orm = self.session.get(CategoryORM, category_id)
        return self._to_domain(orm) if orm else None

    def get_by_slug(self, slug: str) -> Optional[Category]:
        orm = self.session.query(CategoryORM).filter_by(slug=slug).first()
        return self._to_domain(orm) if orm else None

    def list(self) -> List[Category]:
        return [self._to_domain(o) for o in self.session.query(CategoryORM).all()]

    def save(self, category: Category) -> Category:
        if category.id:
            orm = self.session.get(CategoryORM, category.id)
            if orm:
                orm.name = category.name
                orm.slug = category.slug
                orm.description = category.description
        else:
            orm = CategoryORM(
                name=category.name,
                slug=category.slug,
                description=category.description,
            )
            self.session.add(orm)

        self.session.commit()
        return self._to_domain(orm)

    def delete(self, category_id: int) -> None:
        orm = self.session.get(CategoryORM, category_id)
        if orm:
            self.session.delete(orm)
            self.session.commit()

    def _to_domain(self, orm: CategoryORM) -> Category:
        return Category(
            id=orm.id,
            name=orm.name,
            slug=orm.slug,
            description=orm.description,
        )
