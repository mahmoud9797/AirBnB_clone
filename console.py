#!/usr/bin/python3
""" module for console """
import cmd
import json
from models import storage
from models.place import Place
from models.base_model import BaseModel
from models.review import Review
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ class for Airbnb  console """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """ exit from console program """
        return True

    def do_EOF(self, arg):
        """ quit or exit in case of eof or ctrl +D """
        return True

    def emptyline(self):
        """ do nothing if the input is empty line or enter """
        pass

    __classes_dict = {
            "BaseModel",
            "User",
            "City",
            "Place",
            "Review",
            "State",
            "Amenity"
            }

    def do_create(self, arg):
        """ command to create new class instance """
        if not arg:
            print("** class name missing **")
        args_l = arg.split()
        clas_name = args_l[0].strip()
        if clas_name not in HBNBCommand.__classes_dict:
            print("** class doesn't exist **")
        else:
            new_obj = eval(clas_name)()
            print(new_obj.id)
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
