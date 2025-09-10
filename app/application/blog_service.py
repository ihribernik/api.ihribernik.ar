from typing import List

from app.domain.exceptions import PostAlreadyExists
from app.domain.models.post import Post
from app.domain.repositories.post import PostRepository


class BlogService:
    """
    Application service for blog post use cases.
    Coordinates domain logic and repository access.
    """

    def __init__(self, repo: PostRepository) -> None:
        """
        Initialize BlogService with a post repository.
        :param repo: PostRepository implementation
        """
        self.repo = repo

    def create_post(self, title: str, content: str) -> Post:
        """
        Create a new post, raising PostAlreadyExists if title is duplicate.
        :param title: Title of the post
        :param content: Content of the post
        :return: Created Post
        :raises PostAlreadyExists: If a post with the same title exists
        """
        existing = [p for p in self.repo.list() if p.title == title]
        if existing:
            raise PostAlreadyExists(f"A post with title '{title}' already exists.")
        post = Post(id=None, title=title, content=content)
        return self.repo.save(post)

    def list_posts(self) -> List[Post]:
        """
        List all posts.
        :return: List of Post objects
        """
        return self.repo.list()
