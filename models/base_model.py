#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime
from datetime import datetime

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at") and isinstance(value, str):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self, session):
        """Save the current instance to the database."""
        self.updated_at = datetime.utcnow()
        session.add(self)
        session.commit()

    def delete(self, session):
        """Delete the current instance from the database."""
        session.delete(self)
        session.commit()

    def to_dict(self):
        """Generate a dictionary representation of the instance."""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat() if self.created_at else None
        dictionary["updated_at"] = self.updated_at.isoformat() if self.updated_at else None
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    @classmethod
    def find_by_id(cls, session, record_id):
        """Find a record by its ID."""
        return session.query(cls).get(record_id)

    @classmethod
    def find_all(cls, session):
        """Retrieve all records of the model."""
        return session.query(cls).all()
