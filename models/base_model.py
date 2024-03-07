#!/usr/bin/python3
# defines all common attributes/methods for other classes

import uuid
import datetime


class BaseModel:
    """
    defines all common attributes/methods for other classes:

    Attributes:
        id (str): a unique identifier
        created_at (datetime): date of instace creation
        updated_at(datetime): date of instance last update
    """

    def __init__(self):
        """initializes a new BaseModel instance"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """print a string representation of this instance of the class"""

        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at with
        the current datetime
        """

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """

        tmp = self.__dict__
        tmp.__class__ = "BaseModel"
        tmp.created_at = datetime.isoformat(self.created_at)
        tmp.updated_at = datetime.isoformat(self.updated_at)
