from fastapi import FastAPI

# Routes
from src.routes.users import router as users_router
from src.routes.posts import router as posts_router


app = FastAPI()


# Include routes
app.include_router(users_router)
app.include_router(posts_router)