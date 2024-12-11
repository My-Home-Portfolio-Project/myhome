import models
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
import datetime

time = "%d-%m-%Y %H:%M:%S"
Base = declarative_base() if models.storage_t == "db" else object

class BaseModel(Base):
    __tablename__ = "BaseModel"
    id = Column(String(70), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = kwargs.get("id", str(uuid.uuid4()))
        self.created_at = kwargs.get("created_at", datetime.datetime.now())
        self.updated_at = kwargs.get("updated_at", datetime.datetime.now())

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict.pop("_sa_instance_state", None)
        new_dict["created_at"] = self.created_at.strftime(time)
        new_dict["updated_at"] = self.updated_at.strftime(time)
        return new_dict

    def delete(self):
        try:
            models.storage.delete(self)
        except Exception as e:
            print(f"Error deleting object: {e}")
