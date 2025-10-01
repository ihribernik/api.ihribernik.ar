from fastapi import Depends

from app.application.services.post import (
    CreatePost,
    DeletePost,
    GetPostById,
    GetPostBySlug,
    ListPosts,
    UpdatePost,
)
from app.infrastructure.dependencies.respository import (
    get_post_repository,
)
from app.infrastructure.repositories.sqlalchemy.post import SqlAlchemyPostRepository


def get_create_post_service(
    repo: SqlAlchemyPostRepository = Depends(get_post_repository),
) -> CreatePost:
    """
    Dependency to provide a PostService with a repository.
    """
    return CreatePost(repo)


def get_get_post_by_slug_service(
    repo: SqlAlchemyPostRepository = Depends(get_post_repository),
) -> GetPostBySlug:
    """
    Dependency to provide a CategoryService with a repository.
    """
    return GetPostBySlug(repo)


def get_list_post_service(
    repo: SqlAlchemyPostRepository = Depends(get_post_repository),
) -> ListPosts:
    """
    Dependency to provide a ListPostsService with a repository.
    """
    return ListPosts(repo)


def get_get_post_by_id_service(
    repo: SqlAlchemyPostRepository = Depends(get_post_repository),
) -> GetPostById:
    """
    Dependency to provide a GetPostByIdService with a repository.
    """
    return GetPostById(repo)


def get_update_post_service(
    repo: SqlAlchemyPostRepository = Depends(get_post_repository),
) -> UpdatePost:
    """
    Dependency to provide a UpdatePostService with a repository.
    """
    return UpdatePost(repo)


def get_delete_post_service(
    repo: SqlAlchemyPostRepository = Depends(get_post_repository),
) -> DeletePost:
    """
    Dependency to provide a DeletePostService with a repository.
    """
    return DeletePost(repo)
