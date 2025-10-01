from app.application.services.category import (
    ListCategories,
    CreateCategory,
    GetCategoryBySlug,
    GetCategoryById,
    UpdateCategory,
    DeleteCategory,
)
from fastapi import Depends
from app.infrastructure.dependencies.respository import (
    get_category_repository,
)
from app.infrastructure.repositories.sqlalchemy.category import (
    SqlAlchemyCategoryRepository,
)


def get_create_category_service(
    repo: SqlAlchemyCategoryRepository = Depends(get_category_repository),
) -> CreateCategory:
    """
    Dependency to provide a CategoryService with a repository.
    """
    return CreateCategory(repo)


def get_get_category_by_slug_service(
    repo: SqlAlchemyCategoryRepository = Depends(get_category_repository),
) -> GetCategoryBySlug:
    """
    Dependency to provide a CategoryService with a repository.
    """
    return GetCategoryBySlug(repo)


def get_list_category_service(
    repo: SqlAlchemyCategoryRepository = Depends(get_category_repository),
) -> ListCategories:
    """
    Dependency to provide a ListCategoriesService with a repository.
    """
    return ListCategories(repo)


def get_get_category_by_id_service(
    repo: SqlAlchemyCategoryRepository = Depends(get_category_repository),
) -> GetCategoryById:
    """
    Dependency to provide a GetCategoryByIdService with a repository.
    """
    return GetCategoryById(repo)


def get_update_category_service(
    repo: SqlAlchemyCategoryRepository = Depends(get_category_repository),
) -> UpdateCategory:
    """
    Dependency to provide a UpdateCategoryService with a repository.
    """
    return UpdateCategory(repo)


def get_delete_category_service(
    repo: SqlAlchemyCategoryRepository = Depends(get_category_repository),
) -> DeleteCategory:
    """
    Dependency to provide a DeleteCategoryService with a repository.
    """
    return DeleteCategory(repo)
