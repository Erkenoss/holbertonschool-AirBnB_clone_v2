#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City
from sqlalchemy import Column, Integer, String, DateTime, func
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities_relation = relationship(
            "City", backref="state", cascade="all, delete"
            )
    else:
        @property
        def cities(self):
            """ Getter attribute, return the list
            of city instance in state.id """
            from models import storage
            return [city for city in storage.all(City).values() if city.state_id == self.id]
