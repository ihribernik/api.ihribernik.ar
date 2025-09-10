from datetime import datetime
from typing import Optional

from app.domain.models.post import Post
from app.schemas.post import PostSchema


def domain_post_to_schema(post: Post) -> PostSchema:
    return PostSchema(
        title=post.title,
        content=post.content,
        author=post.author,
    )


def schema_to_domain_post(
    schema: PostSchema, id: Optional[int] = None, created_at: Optional[datetime] = None
) -> Post:
    return Post(
        id=id,
        title=schema.title,
        content=schema.content,
        author=schema.author,
        created_at=created_at or datetime.utcnow(),
    )
