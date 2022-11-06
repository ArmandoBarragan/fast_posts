# FastAPI
from fastapi import APIRouter

# Project
from src.schemas import crud_users


router = APIRouter()


# Routes
@router.post('/users/create_account')
def create_account():
    return 'hi'


@router.get('/users/{user_id}')
def user_detail(user_id: int):
    return 'hi'


@router.post('/users/logout')
def logout():
    return 'hi'


@router.patch('/users/{user_id}')
def update_user(user_id: int):
    return 'hi'


@router.delete('/users/{user_id}')
def delete_user(user_id: int):
    return 'hi'