#!/usr/bin/python3
# defines all common attributes/methods for other classes

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    defines all common attributes/methods for other classes:

    Attributes:
        id (str): a unique identifier
        created_at (datetime): date of instace creation
        updated_at(datetime): date of instance last update
    """

    def __init__(self, *args, **kwargs):
        """initializes a new BaseModel instance
        if **kwargs are provided each key,value set will be an attribute,value
        otherwise inialize with new id
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    self[key] = value
            if self.created_at:
                self.created_at = datetime.fromisoformat(self.created_at)
            if self.updated_at:
                self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """print a string representation of this instance of the class"""

        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at with
        the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """

        tmp = {}
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                tmp[key] = value

        return {
            **tmp,
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
            }

    def __setitem__(self, key, value):
        setattr(self, key, value)
