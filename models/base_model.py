#!/usr/bin/python3
""" Basmodel module for whole the program """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ Base model class represents the parent class of the HBNB project """

    def __init__(self, *args, **kwargs):
        """
        constructor
        args: unused
        kwargs: attribute and its value k, v concept
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        time_f = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if (k == 'created_at' or k == 'updated_at'):
                        v = datetime.strptime(v, time_f)
                    else:
                        setattr(self, k, v)
        else:
            models.storage.new(self)

    def save(self):
        """ method used to update the updated date of the object """
        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """
        return the user-readable string for the name of the class
        and its unique id
        and a dictionary containing all attributes
        """
        form_at = "[{}] ({}) {}"
        cl_name = self.__class__.__name__
        return form_at.format(cl_name, self.id, self.__dict__)

    def to_dict(self):
        """ return dictionary representation of the object """
        dic_t = dict(self.__dict__)
        dic_t["__class__"] = self.__class__.__name__
        dic_t["created_at"] = self.created_at.isoformat()
        dic_t["updated_at"] = self.updated_at.isoformat()
        return dic_t
