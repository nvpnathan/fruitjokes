from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from app.db.models import Jokes
from app.schemas.jokes import JokeOutSchema
from app.schemas.token import Status


async def get_jokes():
    return await JokeOutSchema.from_queryset(Jokes.all())


async def get_joke(joke_id) -> JokeOutSchema:
    return await JokeOutSchema.from_queryset_single(Jokes.get(id=joke_id))


async def create_joke(joke, current_user) -> JokeOutSchema:
    joke_dict = joke.dict(exclude_unset=True)
    joke_dict["author_id"] = current_user.id
    joke_obj = await Jokes.create(**joke_dict)
    return await JokeOutSchema.from_tortoise_orm(joke_obj)


async def update_joke(joke_id, joke, current_user) -> JokeOutSchema:
    try:
        db_joke = await JokeOutSchema.from_queryset_single(Jokes.get(id=joke_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Joke {joke_id} not found")

    if db_joke.author.id == current_user.id:
        await Jokes.filter(id=joke_id).update(**joke.dict(exclude_unset=True))
        return await JokeOutSchema.from_queryset_single(Jokes.get(id=joke_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_joke(joke_id, current_user) -> Status:
    try:
        db_joke = await JokeOutSchema.from_queryset_single(Jokes.get(id=joke_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Joke {joke_id} not found")

    if db_joke.author.id == current_user.id:
        deleted_count = await Jokes.filter(id=joke_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Joke {joke_id} not found")
        return Status(message=f"Deleted joke {joke_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")
