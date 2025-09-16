from __future__ import annotations

from typing import List
from typing import Optional

from app.domain.models.tag import Tag
from app.domain.repositories.tag import TagRepository


class CreateTag:
    def __init__(self, repo: TagRepository):
        self.repo = repo

    def execute(self, name: str, slug: str) -> Tag:
        tag = Tag(id=None, name=name, slug=slug)
        return self.repo.save(tag)


class GetTagBySlug:
    def __init__(self, repo: TagRepository):
        self.repo = repo

    def execute(self, slug: str) -> Tag | None:
        return self.repo.get_by_slug(slug)


class ListTags:
    def __init__(self, repo: TagRepository):
        self.repo = repo

    def execute(self) -> list[Tag]:
        return self.repo.list()


class GetTagById:
    def __init__(self, repo: TagRepository):
        self.repo = repo

    def execute(self, tag_id: int) -> Tag | None:
        return self.repo.get_by_id(tag_id)


class UpdateTag:
    def __init__(self, repo: TagRepository):
        self.repo = repo

    def execute(self, tag_id: int) -> Tag | None:
        return self.repo.get_by_id(tag_id)


class DeleteTag:
    def __init__(self, repo: TagRepository):
        self.repo = repo

    def execute(self, tag_id: int) -> None:
        self.repo.delete(tag_id)
