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
        if kwargs:
            for k and v in kwargs.items:
                if k != '__class__' and (k == created_at or k == updated_at):
                    v = strptime(v, time_f)
                    setatrr(self, k, v)
        else:
            id = str(uuid.uuid4())
            curr_date = datetime.now()
            created_at = curr_date
            updated_at = curr_date
