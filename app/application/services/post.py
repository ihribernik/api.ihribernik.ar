from __future__ import annotations

from app.application.services import Service
from app.domain.models.post import PostModel
from app.domain.repositories.post import PostRepository


class CreatePost(Service):
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, title: str, content: str) -> PostModel:
        post = PostModel(
            id=None,
            title=title,
            content=content,
        )
        return self.repo.save(post)


class GetPostBySlug(Service):
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, slug: str) -> PostModel | None:
        return self.repo.get_by_slug(slug)


class ListPosts(Service):
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self) -> list[PostModel]:
        return self.repo.get_all()


class GetPostById(Service):
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, post_id: int) -> PostModel | None:
        return self.repo.get_by_id(post_id)


class UpdatePost(Service):
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, post_id: int) -> PostModel | None:
        return self.repo.get_by_id(post_id)


class DeletePost(Service):
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, post_id: int) -> None:
        self.repo.delete(post_id)
