#!/usr/bin/python3
"""This module defines a Square class"""


class Square():
    """ Class that defines a square"""
    side = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.side * self.side

    def perimeter_of_my_square(self):
        """ Perimeter of the Square """
        return (self.side * 4)

    def __str__(self):
        """ Representation of Square object"""
        return "{}/{}".format(self.side, self.side)

if __name__ == "__main__":

    s = Square(side=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
