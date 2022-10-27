from pydantic import BaseModel
from pydantic import Field


class PostMixin(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    content: str = Field()
    author_pk: int


class CreatePostSchema(PostMixin):
    class Config:
        orm_mode=True


class ReturnPostSchema(PostMixin):
    id: int