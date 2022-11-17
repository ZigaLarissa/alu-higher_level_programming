#!/usr/bin/python3
"""Class that returns the dictionary of attributes of instances"""


class Student:
    """Define class attributes."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Method that retries the attributes dic"""
    def to_json(self, attrs=None):
        dic = self.__dict__

        if attrs is None and type(attrs) != list:
            return(dic)

        else:
            new_dic = dict()
            for item in attrs:
                if item in dic.keys():
                    new_dic[item] = dic[item]
            return(new_dic)

    """Method that replaces all attributes of an instance."""
    def reload_from_json(self, json):
        for item in json.keys():
            self.__dict__[item] = json[item]
