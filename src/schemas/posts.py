# Pydantic
from pydantic import BaseModel
from pydantic import Field

# Project
from src.db import CRUDBase
from src.models import Post

class PostMixin(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    content: str = Field()
    author_pk: int


class CreatePostSchema(PostMixin):
    ...


class UpdatePostSchema(PostMixin):
    id: int

    class Config:
        orm_mode=True

class ReturnPostSchema(PostMixin):
    id: int

    class Config:
        orm_mode=True


class CRUDPost(CRUDBase[Post, CreatePostSchema, UpdatePostSchema]):
    """Inherits from CRUDBasee to make basic transactions for the Post class"""
    ...


crud_posts = CRUDPost(Post)