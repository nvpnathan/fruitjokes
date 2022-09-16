from typing import Optional

from pydantic import BaseModel


# Shared properties
class JokeBase(BaseModel):
    title: str
    description: Optional[str] = None


class Item(JokeBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# Properties to receive on item creation
class JokeCreate(JokeBase):
    title: str


# Properties to receive on item update
class JokeUpdate(JokeBase):
    pass


# Properties shared by models stored in DB
class JokeInDBBase(JokeBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Joke(JokeInDBBase):
    pass


# Properties properties stored in DB
class JokeInDB(JokeInDBBase):
    pass