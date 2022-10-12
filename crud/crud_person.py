from models import Person
from schemas.person import PersonCreate, PersonUpdate

from crud.crud_base import CRUDBase


class CRUDPerson(CRUDBase[Person, PersonCreate, PersonUpdate]):
    pass


person = CRUDPerson(Person)
