from fastapi import Depends

from app.application.services.tag import (
    CreateTag,
    DeleteTag,
    GetTagById,
    GetTagBySlug,
    ListTags,
    UpdateTag,
)
from app.infrastructure.dependencies.respository import get_tag_repository
from app.infrastructure.repositories.sqlalchemy.tag import SqlAlchemyTagRepository


def get_create_tag_service(
    repo: SqlAlchemyTagRepository = Depends(get_tag_repository),
) -> CreateTag:
    """
    Dependency to provide a TagService with a repository.
    """
    return CreateTag(repo)


def get_get_tag_by_slug_service(
    repo: SqlAlchemyTagRepository = Depends(get_tag_repository),
) -> GetTagBySlug:
    """
    Dependency to provide a TagService with a repository.
    """
    return GetTagBySlug(repo)


def get_list_tag_service(
    repo: SqlAlchemyTagRepository = Depends(get_tag_repository),
) -> ListTags:
    """
    Dependency to provide a ListTagsService with a repository.
    """
    return ListTags(repo)


def get_get_tag_by_id_service(
    repo: SqlAlchemyTagRepository = Depends(get_tag_repository),
) -> GetTagById:
    """
    Dependency to provide a GetTagByIdService with a repository.
    """
    return GetTagById(repo)


def get_update_tag_service(
    repo: SqlAlchemyTagRepository = Depends(get_tag_repository),
) -> UpdateTag:
    """
    Dependency to provide a UpdateTagService with a repository.
    """
    return UpdateTag(repo)


def get_delete_tag_service(
    repo: SqlAlchemyTagRepository = Depends(get_tag_repository),
) -> DeleteTag:
    """
    Dependency to provide a DeleteTagService with a repository.
    """
    return DeleteTag(repo)
