class Math:
    @staticmethod
    def add(a, b):
        return a + b



class User:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1


class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
