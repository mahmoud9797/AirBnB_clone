#!/usr/bin/python3
""" module for the city """
from models.base_model import BaseModel


class City(BaseModel):
    """ represnt tha name of the city and state id """

    state_id = ""
    name = ""
