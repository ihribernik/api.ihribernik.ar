from __future__ import annotations

from app.domain.exceptions import InvalidPostError
from app.domain.models.post import Post


class PostService:
    """Reglas de negocio relacionadas con Posts"""

    def validate_post(self, post: Post) -> None:
        if not post.title or len(post.title) < 5:
            raise InvalidPostError(
                'Post title is too short', validation_errors={'title': 'min 5 chars'},
            )

        if not post.content:
            raise InvalidPostError(
                'Post content cannot be empty',
                validation_errors={'content': 'required'},
            )

    def publish_post(self, post: Post) -> Post:
        """Ejemplo: cambiar estado a 'published'"""
        self.validate_post(post)
        post.is_published = True
        return post
