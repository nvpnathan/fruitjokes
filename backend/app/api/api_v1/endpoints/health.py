from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()

@router.get("/")
async def hello_world():
    content = {"message": "Hello, again"}
    response = JSONResponse(content=content)

    return response

@router.get("/ishealthy")
async def health_check():
    return "Health check succeeded\n"
