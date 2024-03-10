#!/usr/bin/python3
"""store dictionary to a file and retrive it"""

import json

class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instance
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return (__objects)

    def new(self, obj):
        """
        create new key value pair in __objects
            key - <class name>.id
            value - obj (i.e the entire obj)
        """

        __objects[f"{obj["__class__"]}.{obj["id"]}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        content = json.dumps(self.__objects)

        try:
            with open(self.__file_path, 'w') as file:
                file.write(content)
        except: Exception as err:
            pass

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no exception will be raised)
        """

        try:
            with open(self.__file_path, 'r') as file:
                return (json.loads(file.read()))
        except: Exception as err:
            pass
