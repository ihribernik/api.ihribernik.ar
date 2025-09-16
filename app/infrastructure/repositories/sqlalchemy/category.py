from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.models.category import CategoryModel
from app.domain.repositories.category import CategoryRepository
from app.infrastructure.database.models import Category as CategoryORM
from app.infrastructure.mappers.category import CategoryMapper


class SqlAlchemyCategoryRepository(CategoryRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, category_id: int) -> Optional[CategoryModel]:
        orm = self.session.get(CategoryORM, category_id)
        return CategoryMapper.to_domain(orm) if orm else None

    def get_by_slug(self, slug: str) -> Optional[CategoryModel]:
        orm = self.session.query(CategoryORM).filter_by(slug=slug).first()
        return CategoryMapper.to_domain(orm) if orm else None

    def get_all(self) -> List[CategoryModel]:
        return [
            CategoryMapper.to_domain(o) for o in self.session.query(CategoryORM).all()
        ]

    def save(self, category: CategoryModel) -> CategoryModel:
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
        return CategoryMapper.to_domain(orm)

    def delete(self, category_id: int) -> None:
        orm = self.session.get(CategoryORM, category_id)
        if orm:
            self.session.delete(orm)
            self.session.commit()
