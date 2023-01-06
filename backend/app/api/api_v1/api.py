from fastapi import APIRouter

from app.api.api_v1.endpoints import users
from app.api.api_v1.endpoints import jokes
from app.api.api_v1.endpoints import health

api_router = APIRouter()
api_router.include_router(users.router, tags=["users"])
api_router.include_router(jokes.router, tags=["jokes"])
api_router.include_router(health.router)
