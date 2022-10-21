from fastapi import APIRouter

router = APIRouter()


# Routes
@router.get('/')
def hi():
    return "Hi"