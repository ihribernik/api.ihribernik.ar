from datetime import datetime, timezone
from typing import Optional

from app.domain.models.post import Post
from app.schemas.post import PostDTO


def domain_post_to_schema(post: Post) -> PostDTO:
    return PostDTO(
        title=post.title,
        content=post.content,
    )


def schema_to_domain_post(
    schema: PostDTO, id: Optional[int] = None, created_at: Optional[datetime] = None
) -> Post:
    return Post(
        id=id,
        title=schema.title,
        content=schema.content,
        created_at=created_at or datetime.now(timezone.utc),
    )
