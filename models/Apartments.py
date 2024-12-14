#!/usr/bin/python3
 from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Apartment(BaseModel):
    """
    Apartment class to represent an apartment.
    """
    __tablename__ = 'apartments'

    name = Column(String(128), nullable=False)  # Apartment name
    apartment_id = Column(String(128), nullable=False, unique=True)  # Unique apartment ID
    rooms_available = Column(Integer, nullable=False, default=0)  # Total rooms available
    rooms_occupied = Column(Integer, nullable=False, default=0)  # Rooms currently occupied
    landlord_id = Column(String(128), ForeignKey('users.id'), nullable=False)  # Landlord ID
    landlord_contact = Column(String(128), nullable=False)  # Landlord contact information

    landlord = relationship('User', back_populates='apartments')  # Relationship to User

    def __init__(self, *args, **kwargs):
        """Initialize the Apartment object."""
        super().__init__(*args, **kwargs)

    def add_rooms(self, num_rooms):
        """
        Add more rooms to the apartment.
        :param num_rooms: Number of rooms to add.
        """
        if num_rooms < 0:
            raise ValueError("Number of rooms to add must be positive.")
        self.rooms_available += num_rooms

    def occupy_room(self, num_rooms):
        """
        Occupy rooms in the apartment.
        :param num_rooms: Number of rooms to occupy.
        """
        if num_rooms <= 0:
            raise ValueError("Number of rooms to occupy must be positive.")
        if self.rooms_occupied + num_rooms > self.rooms_available:
            raise ValueError("Not enough rooms available to occupy.")
        self.rooms_occupied += num_rooms

    def vacate_room(self, num_rooms):
        """
        Vacate rooms in the apartment.
        :param num_rooms: Number of rooms to vacate.
        """
        if num_rooms <= 0:
            raise ValueError("Number of rooms to vacate must be positive.")
        if self.rooms_occupied - num_rooms < 0:
            raise ValueError("Cannot vacate more rooms than are currently occupied.")
        self.rooms_occupied -= num_rooms

    def __str__(self):
        """String representation of the Apartment."""
        return (
            f"Apartment(name={self.name}, apartment_id={self.apartment_id}, "
            f"rooms_available={self.rooms_available}, rooms_occupied={self.rooms_occupied}, "
            f"landlord_id={self.landlord_id}, landlord_contact={self.landlord_contact})"
        )
