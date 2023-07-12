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

    def to_json(self, attr=None):
        """
        Dictionary representation of a Student instance.
        Only return attributes contained in the list `attr`
        """
        obj = self.__dict__
        attr = attr if type(attr) is list else None
        if attr is not None:
            return {k: v for k, v in obj.items() if k in attr}
        return obj


if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
