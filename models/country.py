from models.base_model import BaseModel
from sqlalchemy import Column, String

class Country(BaseModel):
    """
    Country class to represent a country and roles (Tenant or Landlord) in the country.
    """
    __tablename__ = 'countries'

    name = Column(String(128), nullable=False)

    @staticmethod
    def get_countries():
        """Returns a list of predefined countries."""
        return [
            {"id": 1, "name": "Kenya"},
            {"id": 2, "name": "Uganda"},
            {"id": 3, "name": "Tanzania"}
        ]

    def __init__(self, *args, **kwargs):
        """Initialize the Country object."""
        super().__init__(*args, **kwargs)

    def assign_role(self, user, role):
        """
        Assigns a role (Tenant or Landlord) to the user in the country.
        :param user: The user object.
        :param role: 'landlord' or 'tenant'
        """
        if role not in ['landlord', 'tenant']:
            raise ValueError("Invalid role. Choose 'landlord' or 'tenant'.")
        user.role = role
        user.country = self.name

    def __str__(self):
        """String representation of the Country."""
        return f"Country(name={self.name})"
