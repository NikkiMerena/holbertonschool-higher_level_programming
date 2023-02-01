#!/usr/bin/python3
""" Module Rectangle
    creates a Rectangle that inherits from Base """


from models.base import Base


class Rectangle(Base):
    """ describes a Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes a Rectangle instance """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ retrieves width attribute """

        return self.__width

    @property
    def height(self):
        """ retrieves height attribute """

        return self.__height

    @property
    def x(self):
        """ retrieves x attribute """

        return self.__x

    @property
    def y(self):
        """ retrieves y attribute """

        return self.__y

    @width.setter
    def width(self, value):
        """ sets width attribute """

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets height attribute """

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """ sets x attribute """

        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """ sets y attribute """

        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ returns area of the Rectangle """

        return self.__width * self.__height

    def display(self):
        """ displays Rectangle using #'s """

        print('\n' * (self.__y), end="")
        for j in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """ returns string representation of Rectangle """

        return (f'[Rectangle] ({self.id}) '
                f'{self.__x}/{self.__y} - '
                f'{self.__width}/{self.__height}')

    def update(self, *args, **kwargs):
        """ assigns value to an unknown number of arguments """

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "width":
                self.width = value
            if key == "height":
                self.height = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value

    def to_dictionary(self):
        """ return dictionary representation of Rectangle """

        my_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return my_dict
