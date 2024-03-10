#!/usr/bin/python3
""" FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances """
import os.path
from models.base_model import BaseModel
import json
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """class contain methods which
    control sriliztion and deserializtion
    file_path:
    string of the path of the file in which objects stored"
    objects Dictionary of object.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the dictionary of objects """
        return FileStorage.__objects

    def new(self, obj):
        """ method to set obj with key <obj class name>.id """
        cl_name = obj.__class__.__name__
        ke = cl_name + "." + obj.id
        self.__objects.update({ke: obj})

    def save(self):
        """ serialize objects and save it in json file """
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ method used to deserialize json to objects """
        if os.path.isfile(self.__file_path):
            with open (self.__file_path) as f:
                obj_dic = json.load(f)
            for dicts in obj_dic.values():
                clas_name = dicts["__class__"]
                del dicts["__class__"]
                self.new(eval(clas_name)(**dicts))
