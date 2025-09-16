from __future__ import annotations

from typing import List
from typing import Optional

from app.domain.models.post import Post
from app.domain.repositories.post import PostRepository


class CreatePost:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, title: str, content: str, slug: str) -> Post:
        post = Post(
            id=None,
            title=title,
            content=content,
            # slug=slug,
        )
        return self.repo.save(post)


class GetPostBySlug:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, slug: str) -> Post | None:
        return self.repo.get_by_slug(slug)


class ListPosts:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self) -> list[Post]:
        return self.repo.list()


class GetPostById:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, post_id: int) -> Post | None:
        return self.repo.get_by_id(post_id)


class UpdatePost:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, post_id: int) -> Post:
        return self.repo.get_by_id(post_id)


class DeletePost:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, post_id: int) -> None:
        self.repo.delete(post_id)
