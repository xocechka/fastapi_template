from typing import Any

import crud
from db.session import get_session
from fastapi import APIRouter, Depends
from schemas import person as schemas
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/persons",
    tags=["persons"],
)


@router.get("/{id}", response_model=schemas.Person | None)
async def read_person(
    id: int,
    db: Session = Depends(get_session)
) -> Any:
    return crud.person.get(db=db, id=id)


@router.get("/", response_model=list[schemas.Person])
async def read_persons(
    db: Session = Depends(get_session)
) -> Any:
    return crud.person.get_multi(db)


@router.post("/", response_model=schemas.Person)
async def create_person(
    person: schemas.PersonCreate,
    db: Session = Depends(get_session)
) -> Any:
    return crud.person.create(db=db, obj_in=person)


@router.put("/", response_model=schemas.Person)
async def update_person(
    person: schemas.PersonUpdate,
    id: int,
    db: Session = Depends(get_session)
) -> Any:
    return crud.person.update(db=db, obj_in=person, target_id=id)


@router.delete("/", response_model=schemas.Person)
async def delete_person(
    id: int,
    db: Session = Depends(get_session)
) -> Any:
    return crud.person.remove(db=db, id=id)
