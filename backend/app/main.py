import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.db.register import register_tortoise
from app.core.config import settings, TORTOISE_ORM
from app.api.api_v1.api import api_router


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=True)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
