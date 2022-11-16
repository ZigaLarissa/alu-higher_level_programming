#!/usr/bin/python3
'''Class Rectangle that inherits from BaseGeometry (7-base_geometry.py)'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class that inherits the BaseGeometry '''

    def __init__(self, width, height):
        '''A function that created a rectangle '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
