from db.base_class import Base
from sqlalchemy import Column, Integer, String


class Person(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
