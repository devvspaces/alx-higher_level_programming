#!/usr/bin/python3

"""
IO module
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """
        __init__ method

        :param first_name: student's first name
        :type first_name: str
        :param last_name: student's last name
        :type last_name: str
        :param age: student's age
        :type age: int
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Dictionary representation of a Student instance
        """
        return self.__dict__


if __name__ == "__main__":
    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))
