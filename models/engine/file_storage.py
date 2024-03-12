#!/usr/bin/python3
"""store dictionary to a file and retrive it"""

import json
from models.base_model import BaseModel

class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instance
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return (self.__objects)

    def new(self, obj):
        """
        create new key value pair in __objects
            key - <class name>.id
            value - obj (i.e the entire obj)
        """

        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        tmp = {}

        for key,value in self.__objects.items():
            tmp[key] = self.__objects[key].to_dict()
        content = json.dumps(tmp)

        try:
            with open(self.__file_path, 'w') as file:
                file.write(content)
        except Exception as err:
            pass

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no exception will be raised)
        """

        try:
            with open(self.__file_path, 'r') as file:
                dict1 = json.load(file)

                for obj in dict1.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except Exception as err:
            pass
