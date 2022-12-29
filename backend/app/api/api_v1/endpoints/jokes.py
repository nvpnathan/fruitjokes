from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import app.crud.jokes as crud
from app.auth.jwthandler import get_current_user
from app.schemas.jokes import JokeOutSchema, JokeInSchema, UpdateJoke
from app.schemas.token import Status
from app.schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/jokes",
    response_model=List[JokeOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_jokes():
    return await crud.get_jokes()


@router.get(
    "/joke/{joke_id}",
    response_model=JokeOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_joke(joke_id: int) -> JokeOutSchema:
    try:
        return await crud.get_joke(joke_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Joke does not exist",
        )


@router.post(
    "/joke", response_model=JokeOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_joke(
    joke: JokeInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> JokeOutSchema:
    return await crud.create_joke(joke, current_user)


@router.patch(
    "/joke/{joke_id}",
    dependencies=[Depends(get_current_user)],
    response_model=JokeOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_joke(
    joke_id: int,
    joke: UpdateJoke,
    current_user: UserOutSchema = Depends(get_current_user),
) -> JokeOutSchema:
    return await crud.update_joke(joke_id, joke, current_user)


@router.delete(
    "/joke/{joke_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_joke(
    joke_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_joke(joke_id, current_user)