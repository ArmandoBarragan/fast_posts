from fastapi import APIRouter

router = APIRouter()


# Routes
@router.get('/hello')
def hello():
    return "Hi"