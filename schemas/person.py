from fastapi_utils.api_model import APIModel


class PersonBase(APIModel):
    name: str


class PersonCreate(PersonBase):
    pass


class PersonUpdate(PersonBase):
    pass


class Person(PersonBase):
    id: int
