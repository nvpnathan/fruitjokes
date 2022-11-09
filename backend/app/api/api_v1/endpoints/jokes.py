from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/my-jokes", response_model=List[schemas.Joke])
def read_jokes(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve jokes.
    """
    if crud.user.is_superuser(current_user):
        jokes = crud.joke.get_multi(db, skip=skip, limit=limit)
    else:
        jokes = crud.joke.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return jokes


@router.post("/", response_model=schemas.Joke)
def create_joke(
    *,
    db: Session = Depends(deps.get_db),
    joke_in: schemas.JokeCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new joke.
    """
    joke = crud.joke.create_with_owner(db=db, obj_in=joke_in, owner_id=current_user.id)
    return joke


@router.put("/{id}", response_model=schemas.Joke)
def update_joke(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    joke_in: schemas.JokeUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a joke.
    """
    joke = crud.joke.get(db=db, id=id)
    if not joke:
        raise HTTPException(status_code=404, detail="Joke not found")
    if not crud.user.is_superuser(current_user) and (joke.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    joke = crud.joke.update(db=db, db_obj=joke, obj_in=joke_in)
    return joke


@router.get("/{id}", response_model=schemas.Joke)
def read_joke(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get joke by ID.
    """
    joke = crud.joke.get(db=db, id=id)
    if not joke:
        raise HTTPException(status_code=404, detail="Joke not found")
    if not crud.user.is_superuser(current_user) and (joke.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return joke


@router.delete("/{id}", response_model=schemas.Joke)
def delete_joke(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a joke.
    """
    joke = crud.joke.get(db=db, id=id)
    if not joke:
        raise HTTPException(status_code=404, detail="Joke not found")
    if not crud.user.is_superuser(current_user) and (joke.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    joke = crud.joke.remove(db=db, id=id)
    return joke
