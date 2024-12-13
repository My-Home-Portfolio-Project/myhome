#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.apartment import Apartment

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists).
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                objects = json.load(f)
                for key, value in objects.items():
                    class_name = value['__class__']
                    if class_name in globals():
                        self.__objects[key] = globals()[class_name](**value)
        except FileNotFoundError:
            pass

# Ensure all new classes are recognized by FileStorage
globals().update({
    'BaseModel': BaseModel,
    'User': User,
    'Apartment': Apartment
})
