#!/usr/bin/python3
""" modeule for reveiw """
from models.base_model import BaseModel


class Review(BaseModel):
    """ represnt the client review """

    place_id = ""
    user_id = ""
    text = ""
