import os


def get_age():
    with open("app.py", 'r') as f:
        code = f.read()
    f.close()
    return str(code)


class Animal:
    _all = []

    def __new__(cls, gender, legs_count, has_wings, age=0, *args, name=None, **kwargs):
        newAnimal = super(Animal, cls).__new__(cls, *args, **kwargs)
        Animal._all.append(newAnimal)
        return newAnimal

    def __init__(self, gender, legs_count, has_wings, age=0, *args, name=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._age = age
        self.gender = gender
        self.legs_count = legs_count
        self.has_wings = has_wings

    @classmethod
    def add_year(cls):
        for everyAnimal in cls._all:
            everyAnimal.age += 1
            print(everyAnimal.age)
        pass

    @property
    def age(self):
        return self._age

    def __class__(self):
        return str(type(self).__name__.lower())

    @age.setter
    def age(self, age):
        self._age = age


class Pet(Animal):
    def __init__(self, *args, name=None, **kwargs):
        if name is None:
            raise ValueError('Pet should have a name')
        super().__init__(*args, **kwargs)
        self.name = name


class Bird(Animal):
    legs_count = 2
    has_wings = True


class Cat(Pet):
    pass


class Dog(Pet):
    pass


class Parrot(Pet, Bird):
    pass


class Duck(Bird):
    pass

