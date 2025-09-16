from __future__ import annotations

from app.domain.models.post import PostModel
from app.domain.repositories.post import PostRepository


class PostService:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def get_all(self) -> list[PostModel]:
        return self.repo.get_all()

    def get_by_id(self, post_id: int) -> PostModel | None:
        return self.repo.get_by_id(post_id)

    def get_by_slug(self, slug: str) -> PostModel | None:
        return self.repo.get_by_slug(slug)

    def create(self, title: str, content: str) -> PostModel:
        return self.repo.save(PostModel(id=None, title=title, content=content))

    def delete(self, post_id: int) -> None:
        self.repo.delete(post_id)

    def update(self, post_id: int, title: str, content: str) -> PostModel | None:
        return self.repo.save(PostModel(id=post_id, title=title, content=content))


class CreatePost:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, title: str, content: str) -> PostModel:
        post = PostModel(
            id=None,
            title=title,
            content=content,
        )
        return self.repo.save(post)


class GetPostBySlug:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, slug: str) -> PostModel | None:
        return self.repo.get_by_slug(slug)


class ListPosts:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self) -> list[PostModel]:
        return self.repo.get_all()


class GetPostById:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, post_id: int) -> PostModel | None:
        return self.repo.get_by_id(post_id)


class UpdatePost:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, post_id: int) -> PostModel | None:
        return self.repo.get_by_id(post_id)


class DeletePost:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, post_id: int) -> None:
        self.repo.delete(post_id)
