#!/usr/bin/python3

"""
Base class module
"""

import json
import turtle
import random


class Base:
    """Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """init method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries
        """
        if not list_dictionaries:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def to_csv_string(cls, list_dictionaries):
        """CSV string representation of list_dictionaries
        """
        if not list_dictionaries:
            list_dictionaries = []

        result = ""

        # Specify keys
        keys = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Square":
            keys = ["id", "size", "x", "y"]

        # Ensure they are added in the correct order
        for _dict in list_dictionaries:
            result += ",".join([str(_dict.get(key, 0)) for key in keys]) + "\n"

        return result

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file

        :param list_objs: list of instances who inherits of Base
        :type list_objs: list
        """
        if not list_objs:
            list_objs = []

        dicts = [x.to_dictionary() for x in list_objs]
        strs = cls.to_json_string(dicts)
        file_name = cls.__name__ + ".json"

        with open(file_name, "w") as f:
            f.write(strs)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string

        :param json_string: string representing a list of dictionaries
        :type json_string: str
        """
        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
            dummy.update(**dictionary)
        else:
            dummy = cls(1)
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load instances from JSON file
        """
        instances = []
        read_str = ""
        filename = cls.__name__ + ".json"

        # Try to read from file
        try:
            with open(filename) as f:
                read_str = f.read()
        except FileNotFoundError:
            return instances

        # Create instances
        list_of_dicts = cls.from_json_string(read_str)
        for _dict in list_of_dicts:
            instances.append(cls.create(**_dict))

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        writes the CSV string representation of list_objs to a file

        :param list_objs: list of instances who inherits of Base
        :type list_objs: list
        """
        if not list_objs:
            list_objs = []

        dicts = [x.to_dictionary() for x in list_objs]
        strs = cls.to_csv_string(dicts)
        file_name = cls.__name__ + ".csv"

        with open(file_name, "w") as f:
            f.write(strs)

    @classmethod
    def load_from_file_csv(cls):
        """Load instances from CSV file
        """

        instances = []
        filename = cls.__name__ + ".csv"

        # Try to read from file
        try:
            with open(filename) as f:
                lines = [x.split(',') for x in f.readlines()]

                # Specify keys
                keys = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    keys = ["id", "size", "x", "y"]

                # Create instances
                for row in lines:
                    _dict = {k:  int(v) for k, v in zip(keys, row)}
                    instances.append(cls.create(**_dict))
        except FileNotFoundError:
            pass

        return instances

    @staticmethod
    def random_color():
        chars = "abcdef0123456789"
        return "#" + "".join(random.choices(chars, k=6))

    @staticmethod
    def draw(list_rectangles, list_squares):

        # maximize screen
        screen = turtle.Screen()
        screenTk = screen.getcanvas().winfo_toplevel()
        screenTk.attributes("-zoom", 1)

        canvwidth, canvheight = turtle.screensize()

        def set_turtle():
            turtle.hideturtle()
            turtle.pensize(5)
            turtle.penup()
            turtle.goto(-canvwidth, canvheight)
            turtle.pendown()

        set_turtle()

        for index, shape in enumerate(list_rectangles + list_squares):
            turtle.color(Base.random_color())
            turtle.title("Drawing shapes: {}/{}".format(index +
                         1, len(list_rectangles + list_squares)))
            turtle.penup()
            turtle.fd(shape.x)
            turtle.right(90)
            turtle.fd(shape.y)
            turtle.left(90)
            turtle.pendown()
            turtle.write(str(shape), font=("Verdana", 12, "normal"))
            turtle.fd(shape.width)
            turtle.rt(90)
            turtle.fd(shape.height)
            turtle.rt(90)
            turtle.fd(shape.width)
            turtle.rt(90)
            turtle.fd(shape.height)
            turtle.rt(90)
            turtle.clear()
            set_turtle()

        turtle.exitonclick()
