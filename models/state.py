#!/usr/bin/python3
"""This is the state class"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """Represente the state class as states table on the db"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan', backref="state")

    @property
    def cities(self):
        dic = models.storage.all()
        lista = []
        result = []
        for key in dic:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(dic[key])
        for elem in lista:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
