#!/usr/bin/python3
#entry point of the command interpreter:

import cmd

from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    a command interpreter
    """

    prompt = "(hbnb)"
    __allowed_classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def do_quit(self, arg):
        """exits the program. you can also use 'EOF'"""
        return True

    def do_EOF(self, arg):
        """exits the program. you can also use 'quitg"""
        return True

    def emptyline(self):
        """ignore impty line"""

        pass

    @staticmethod
    def no_class(arg):
        """checks if classname does not exist. and return false if exists"""

        if not arg:
            print("** class name missing **")
            return (True)
        if arg not in self.__allowed_classes:
            print("** class doesn't exist **")
            return (True)
        return (False)

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        """

        if (self.no_class(arg)):
            return
        tmp = BaseModel()
        storage.save()
        print(tmp.id)

    @staticmethod
    def no_id(args):
        """check if id does not exist. and return false if exists"""

        tmp = storage.all()
        if len(args) == 1:
            print("** instance id missing **")
            return (True)
        elif f"{args[0]}.{args[1]}" not in tmp:
            print("** no instance found **")
            return (True)
        return (False)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id. Ex: $ show BaseModel 1234-1234-1234.
        """

        tmp = storage.all()
        if not arg:
            self.no_class(arg)
            return
        args = arg.split()

        if (self.no_class(args[0])):
            return
        if (self.no_id(args)):
            return
        print(tmp[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """

        tmp = storage.all()
        if not arg:
            self.no_class(arg)
            return
        args = arg.split()

        if (self.no_class(args[0])):
            return
        if (self.no_id(args)):
            return
        del tmp[f"{args[0]}.{args[1]}"]
        storage.save()

    def do_all(self, arg):
        """print all"""

        if not arg:
            self.no_class(arg)
            return
        args = arg.split()
        objs = []
        for obj in storage.all().values():
            if len(args) > 0 and args[0] == obj.__class__.__name__:
                objs.append(obj.__str__())
            elif len(args) == 0:
                objs.append(obj.__str__())
        print(objs)

    def do_update(self, arg):
        """
        update instance
        usage: update <class> <id>
        """

        if not arg:
            self.no_class(arg)
            return
        args = arg.split()
        if (self.no_class(args[0])):
            return
        if (self.no_id(args)):
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return False
        elif len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        elif len(args) == 4:
            obj = objdict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objdict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                k_in_keys = k in obj.__class__.__dict__.keys()
                type_in = type(obj.__class__.__dict__[k]) in {str, int, float}
                if (k_in_keys and type_in):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
