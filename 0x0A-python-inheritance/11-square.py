#!/usr/bin/python3
"""Project 0x07 Task 2"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ The Square Squared Squares, aslo private member size is redundent"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self) -> str:
        """Ideally this would be handled diffrently in the base class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
