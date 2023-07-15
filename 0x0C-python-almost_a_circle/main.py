#!/usr/bin/python3

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import random


if __name__ == "__main__":
    obj = Base()

    list_rectangles = []
    for _ in range(10):
        width = random.randint(20, 100)
        height = random.randint(20, 100)
        x = random.randint(0, 40)
        y = random.randint(0, 40)
        rectangle = Rectangle(width, height, x, y)
        list_rectangles.append(rectangle)

    list_squares = []
    for _ in range(10):
        size = random.randint(20, 100)
        x = random.randint(0, 40)
        y = random.randint(0, 40)
        square = Square(size, x, y)
        list_squares.append(square)

    obj.draw(list_rectangles, list_squares)
