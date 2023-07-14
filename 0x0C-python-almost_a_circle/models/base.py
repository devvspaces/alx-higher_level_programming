#!/usr/bin/python3

"""
Base class module
"""

import json


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

    @staticmethod
    def to_csv_string(list_dictionaries):
        """CSV string representation of list_dictionaries
        """
        if not list_dictionaries:
            list_dictionaries = []
        return ",".join(list_dictionaries)

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
        pass
