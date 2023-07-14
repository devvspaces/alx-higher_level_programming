#!/usr/bin/python3

"""
Rectangle class module
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter method """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter method

        :param value: value to set
        :type value: int
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """height getter method """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter method

        :param value: value to set
        :type value: int
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """x getter method """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter method

        :param value: value to set
        :type value: int
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """y getter method """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter method

        :param value: value to set
        :type value: int
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """area method
        """
        return self.width * self.height

    def display(self):
        """Print out the rectangle in stdout
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """
        Nice output format

        :return: str representation of the object
        :rtype: str
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Update the rectangle
        """
        if args:
            keys = ["id", "width", "height", "x", "y"]
            for key, value in zip(keys, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of a Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
