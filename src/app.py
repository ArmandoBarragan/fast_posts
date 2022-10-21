from fastapi import FastAPI

# Routes
from src.routes.users import router as users_router


app = FastAPI()


# Include routes
app.include_router(users_router)
