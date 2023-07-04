#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0) -> None:
        """
        Rectangle class init method

        :param width: width, defaults to 0
        :type width: int, optional
        :param height: height, defaults to 0
        :type height: int, optional
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle

        :param value: width value
        :type value: int
        :raises TypeError: width must be an integer
        :raises ValueError: width must be >= 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle

        :param value: height value
        :type value: int
        :raises TypeError: height must be an integer
        :raises ValueError: height must be >= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Get the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Get the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """
        Informal representation of this object
        """
        result = []

        if self.width == 0 or self.height == 0:
            return ""

        for _ in range(self.height):
            start = ""
            for _ in range(self.width):
                start += "#"
            result.append(start)
        return "\n".join(result)

    def __repr__(self) -> str:
        """
        Formal representation of this object
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Delete this object
        """
        print("Bye rectangle...")
