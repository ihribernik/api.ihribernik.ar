from __future__ import annotations

from app.application.services import Service
from app.domain.models.tag import TagModel
from app.domain.repositories.tag import TagRepository


class CreateTag(Service):
    def __init__(self, repo: TagRepository):
        self.repo = repo

    def execute(self, name: str, slug: str) -> TagModel:
        tag = TagModel(id=None, name=name, slug=slug)
        return self.repo.save(tag)


class GetTagBySlug(Service):
    def __init__(self, repo: TagRepository):
        self.repo = repo

    def execute(self, slug: str) -> TagModel | None:
        return self.repo.get_by_slug(slug)


class ListTags(Service):
    def __init__(self, repo: TagRepository):
        self.repo = repo

    def execute(self) -> list[TagModel]:
        return self.repo.get_all()


class GetTagById(Service):
    def __init__(self, repo: TagRepository):
        self.repo = repo

    def execute(self, tag_id: int) -> TagModel | None:
        return self.repo.get_by_id(tag_id)


class UpdateTag(Service):
    def __init__(self, repo: TagRepository):
        self.repo = repo

    def execute(self, tag_id: int) -> TagModel | None:
        return self.repo.get_by_id(tag_id)


class DeleteTag(Service):
    def __init__(self, repo: TagRepository):
        self.repo = repo

    def execute(self, tag_id: int) -> None:
        self.repo.delete(tag_id)
