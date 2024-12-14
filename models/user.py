#!/usr/bin/python3
from models.base_model import BaseModel
from sqlalchemy import Column, String

class User(BaseModel):
    """
    User class that inherits from BaseModel.
    Represents a user who can be either a landlord or a tenant.
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False, default="")
    password = Column(String(128), nullable=False, default="")
    first_name = Column(String(128), default="")
    last_name = Column(String(128), default="")
    role = Column(String(50), default=None)  # Role can be 'landlord' or 'tenant'

    def set_role(self, role):
        """
        Update the user's role.
        :param role: 'landlord' or 'tenant'
        """
        if role in ['landlord', 'tenant']:
            self.role = role
        else:
            raise ValueError("Invalid role. Choose 'landlord' or 'tenant'.")

    def is_landlord(self):
        """Check if the user is a landlord."""
        return self.role == 'landlord'

    def is_tenant(self):
        """Check if the user is a tenant."""
        return self.role == 'tenant'
