#!/usr/bin/python3
""" Module base
    defines Base class for other classes in this project """


import json


class Base:
    """ class with private attribute
        __nb_objects """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization of a Base instance """

        if type(id) != int and id is not None:
            raise TypeError('id must be an integer')
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON str representation of list_dictionaries """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON str to file """

        dict_list = []
        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())

        with open(cls.__name__+".json", 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns list of JSON str representation """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2, 0)
        else:
            dummy = cls(1, 0)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """

        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                json_string = f.read()
                dict_list = []
            for obj in cls.from_json_string(json_string):
                dict_list.append(cls.create(**obj))
        except:
            dict_list = []
        return dict_list
