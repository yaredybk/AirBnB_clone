#!/usr/bin/python3
#entry point of the command interpreter:

import cmd
from models.base_model import BaseModel
from models.__init__ import storage

class HBNBCommand(cmd.Cmd):
    """
    a command interpreter
    """

    intro = "welcome to hbnb console"
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """exits the program. you can also use 'EOF'"""
        return True

    def do_EOF(self, arg):
        """exits the program. you can also use 'quit'"""
        return True

    def emptyline(self):
        """ignore impty line"""

        pass

    @staticmethod
    def no_class(arg):
        """checks if classname exists"""

        if not arg:
            print("** class name missing **")
            return (True)
        if arg != "BaseModel":
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
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in tmp:
            print("** no instance found **")
        else:
            print(tmp[f"{args[0]}.{args[1]}"])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
