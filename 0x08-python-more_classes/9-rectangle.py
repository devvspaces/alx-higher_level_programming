#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """
    A class to represent a rectangle.

    :param number_of_instances: number of instances
    :type number_of_instances: int
    :param print_symbol: symbol used for string representation
    :type print_symbol: str
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Rectangle class init method

        :param width: width, defaults to 0
        :type width: int, optional
        :param height: height, defaults to 0
        :type height: int, optional
        """
        self.__class__.number_of_instances += 1
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
                start += str(self.print_symbol)
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
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Get the biggest rectangle based on the area

        :param rect_1: first rectangle
        :type rect_1: Rectangle
        :param rect_2: second rectangle
        :type rect_2: Rectangle
        :return: biggest rectangle
        :rtype: Rectangle
        :raises TypeError: rect_1 must be an instance of Rectangle
        :raises TypeError: rect_2 must be an instance of Rectangle
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new square using size attribute

        :param size: size of the square, defaults to 0
        :type size: int, optional
        :return: new square with width and height equal to size
        :rtype: Rectangle
        """
        return cls(size, size)
