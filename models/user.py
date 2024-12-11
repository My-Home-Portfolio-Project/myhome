#!/usr/bin/python3
from sqlalchemy import Column, String
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
from models.base_model import BaseModel, Base
from os import getenv
import models

storage_t = getenv('HBNB_TYPE_STORAGE')

if storage_t == 'db':
    class User(BaseModel, Base):
        """User class for database storage"""
        __tablename__ = 'users'
        email = Column(String(128), nullable=False, unique=True)
        password_hash = Column(String(128), nullable=False)

        def set_password(self, password):
            """Hash and set the user's password"""
            self.password_hash = generate_password_hash(password)

        def check_password(self, password):
            """Verify the user's password"""
            return check_password_hash(self.password_hash, password)
else:
    class User(BaseModel):
        """User class for file storage"""
        email = ""
        password_hash = ""

        def set_password(self, password):
            """Hash and set the user's password"""
            self.password_hash = generate_password_hash(password)

        def check_password(self, password):
            """Verify the user's password"""
            return check_password_hash(self.password_hash, password)

# Example usage
if __name__ == "__main__":
    # Create a new user account
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check if user already exists
    existing_users = [user for user in models.storage.all('User').values() if user.email == email]
    if existing_users:
        print("User already exists. Please log in.")
    else:
        user = User(email=email)
        user.set_password(password)
        models.storage.new(user)
        models.storage.save()
        print("Account created successfully!")

    # Login process
    email = input("Enter your email to log in: ")
    password = input("Enter your password: ")

    user = next((u for u in models.storage.all('User').values() if u.email == email), None)
    if user and user.check_password(password):
        print("Login successful!")
    else:
        print("Invalid email or password.")
