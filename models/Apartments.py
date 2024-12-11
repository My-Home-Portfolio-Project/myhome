#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


storage_t = getenv('HBNB_TYPE_STORAGE')


if storage_t == 'db':
    class Apartment(BaseModel, Base):
        """Apartment class for database storage"""
        __tablename__ = 'apartments'
        name = Column(String(128), nullable=False)
        country_id = Column(String(70), ForeignKey('countries.id'), nullable=False)
        # Add other apartment attributes as necessary
else:
    class Apartment(BaseModel):
        """Apartment class for file storage"""
        name = ""
        country_id = ""

        @property
        def country(self):
            """Retrieve the Country instance associated with this apartment"""
            all_countries = models.storage.all('Country')
            return all_countries.get(self.country_id)

# Update the Country model to include a relationship or property for apartments
if storage_t == 'db':
    from models.country import Country

    Country.apartments = relationship('Apartment', backref='country', cascade='all, delete')
else:
    from models.country import Country

    @property
    def apartments(self):
        """Return a list of apartments associated with the country"""
        return [apt for apt in models.storage.all('Apartment').values() if apt.country_id == self.id]

    Country.apartments = apartments
