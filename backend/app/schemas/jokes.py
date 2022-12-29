from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.db.models import Jokes


JokeInSchema = pydantic_model_creator(
    Jokes, name="JokeIn", exclude=["author_id"], exclude_readonly=True)
JokeOutSchema = pydantic_model_creator(
    Jokes, name="Joke", exclude=[
      "modified_at", "author.password", "author.created_at", "author.modified_at"
    ]
)


class UpdateJoke(BaseModel):
    title: Optional[str]
    content: Optional[str]
