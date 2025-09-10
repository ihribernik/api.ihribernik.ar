from typing import List, Optional

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

    def execute(self, slug: str) -> Optional[Tag]:
        return self.repo.get_by_slug(slug)


class ListTags:
    def __init__(self, repo: TagRepository):
        self.repo = repo

    def execute(self) -> List[Tag]:
        return self.repo.list()
