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
     
    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

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

    def do_show(self, arg):
        """ show info about an object based on class name & id"""
        if not arg:
            print("** class name missing **")
            return

        args_l = arg.split()
        class_name = args_l[0].strip()
        if class_name not in HBNBCommand.__classes_dict:
            print("** class doesn't exist **")
            return

        if len(args_l) < 2:
            print("** instance id missing **")
            return

        obj_id = args_l[1].strip()
        k = "{}.{}".format(class_name, obj_id)
        obj_s = storage.all()
        if k not in obj_s:
            print("** no instance found **")
            return
        print(obj_s[k])

    def do_destroy(self, arg):
        """ command used to delete object based on class and id """
        if arg == "":
            print("** class name missing **")
            return
        args_l = arg.split()
        clas_name = args_l[0].strip()
        if clas_name not in HBNBCommand.__classes_dict:
            print("** class doesn't exist **")
            return
        if len(args_l) < 2:
            print("** instance id missing **")
            return
        obj_id = args_l[1].strip()
        k = "{}.{}".format(clas_name, obj_id)
        obj_s = storage.all()
        if k not in obj_s:
            print("** no instance found **")
            return
        del obj_s[k]
        storage.save()
    
    def do_all(self, arg):
        """ print a list of all objects based or not class"""
        args_l = arg.split()
        if len(args_l) > 0 and args_l[0] not in HBNBCommand.__classes_dict:
            print("** class doesn't exist **")
        else:
            obj_s = storage.all()
            store_l = []
            for obj in obj_s.values():
                if len(args_l) > 0 and args_l[0] == obj.__class__.__name__:
                    store_l.append(obj.__str__())
                elif len(args_l) == 0:
                    store_l.append(obj.__str__())
            print(store_l)

    def do_update(self, arg):
        """ set the attribute value based on class name id """
        if arg == "":
            print("** class name missing **")
            return
        args_l = arg.split()
        clas_name = args_l[0].strip()
        if clas_name not in HBNBCommand.__classes_dict:
            print("** class doesn't exist **")
            return
        if len(args_l) < 2:
            print("** instance id missing **")
            return
        obj_id = args_l[1].strip()
        obj_s = storage.all()
        k = "{}.{}".format(clas_name, obj_id)
        if k not in obj_s:
            print("** no instance found **")
            return
        if len(args_l) < 3:
            print("** attribute name missing **")
            return
        attr_name = args_l[2].strip()
        if len(args_l) < 4:
            print("** value missing **")
            return
        attr_value = args_l[3].strip()
        obj = obj_s[k]
        attr_type = type(getattr(obj, attr_name))
        casted_v = attr_type(attr_value)
        setattr(obj, attr_name, casted_v)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
