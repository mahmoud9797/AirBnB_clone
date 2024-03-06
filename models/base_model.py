#!/usr/bin/python3
""" Basmodel module for whole the program """

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ Base model class represent the parent class of HBNB project """

    def __init__(self, *args, **kwargs):
        """ constructor """

        """
        args : unused
        kwargs : attributt and its value k and v concept
        """
        time_f = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs != 0:
            for k, v in kwargs.items():
                if k != '__class__':
                    if (k == "created_at" or k == "updated_at"):
                        v = datetime.strptime(v, time_f)
                        setattr(self, k, v)
        else:
            self.id = str(uuid4())
            curr_date = datetime.now()
            self.created_at = curr_date
            self.updated_at = curr_date

    def save(self):
        """ method used to update the the updated date of object """
        self.updated_at = datetime.now()

    def __str__(self):
        """
        return user readable string for the name of calss and its unique id
        and dictionary contains all attributes
        """
        form_at = "[{}] ({}) {}"
        cl_name = self.__class__.__name__
        return form_at.format(cl_name, self.id, self.__dict__)

    def to_dict(self):
        """ return dictionary representation of the object """
        dic_t = {**self.__dict__}
        dic_t["__class__"] = self.__class__.__name__
        dic_t["created_at"] = self.created_at.isoformat()
        dic_t["updated_at"] = self.updated_at.isoformat()
        return dic_t
