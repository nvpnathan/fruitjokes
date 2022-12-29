from fastapi import APIRouter

from app.api.api_v1.endpoints import users
from app.api.api_v1.endpoints import jokes

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(jokes.router)
