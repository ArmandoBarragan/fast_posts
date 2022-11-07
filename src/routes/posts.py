# FastAPI
from fastapi import APIRouter

# Project
from src.schemas import crud_posts
from src.schemas import CreatePostSchema
from src.schemas import ReturnPostSchema
from src.schemas import UpdatePostSchema


router = APIRouter()


@router.post('/posts/create',
             tags=['posts'])
def create_post():
    return 'hi'


@router.get('/posts/{post_id}',
            tags=['posts'])
def post_detail(post_id: int):
    return 'hi'


@router.patch('/posts/{post_id}',
              tags=['posts'])
def update_post(post_int: int):
    return 'hi'


@router.delete('/posts/{post_id}',
               tags=['posts'])
def delete_post(post_id: int):
    return 'hi'