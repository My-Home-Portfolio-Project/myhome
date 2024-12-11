#!/usr/bin/python3
"""Module for Country class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

if models.storage_t == 'db':
    class Country(BaseModel, Base):
        """Country class"""
        __tablename__ = 'countries'
        name = Column(String(128), nullable=False)
        states = relationship('State', backref='country', cascade='all, delete')
else:    
    class Country(BaseModel):
        """Country class"""
        name = ""

        @property
        def states(self):
            """Return the list of State instances with the country_id"""
            return [state for state in models.storage.all('State').values()
                    if state.country_id == self.id]