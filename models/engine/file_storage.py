#!/usr/bin/env python3
"""serializes and deserializes objects to
and from json
"""

import json


class FileStorage:
    """defined a class to serialize and
    deserialize json
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as f:

            json.dump(my_dict, f)

    def reload(self):
        """deserializes from a json file
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }
        obj = {}
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_data = json.load(f)
                for key, value in json_data.items():
                    obj[key] = class_dict[value["__class__"]](**value)
                FileStorage.__objects = obj
        except FileNotFoundError:
            pass
