#!/usr/bin/python3
""" module for user class """
from models.base_model import BaseModel


class User(BaseModel):
    """ user class
    email: the user email
    password : the user password
    first_name: the user first name
    last_name: the user last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
