import datetime
from typing import NamedTuple
from abc import ABCMeta, abstractmethod

class HogwartsMember:
    """
    Creates a member of the Hogwarts School of Witchcraft and Wizardry
    """

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}

    def whisper(function):
        def wrapper(self, *args):
            original_output = function(self, *args)
            first_part, words = original_output.split(' says: ')
            words = words.replace('!', '.')
            new_output = f"{first_part} whispers: {words}.."
            return new_output
        return wrapper

    @whisper
    def says(self, words):
        return f"{self._name} says: {words}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})"


class Pupil(HogwartsMember):
    """
    Create a Hogwarts Pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, house: str, start_year: int, pet: tuple = None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year
        self.known_spells = set()

        if pet is not None:
            self.pet_name, self.pet_type = pet

    @classmethod
    def ginny(cls):
        return cls('Ginevra Weasley', 1981, 'female', 'Gryffindor', 1992)


if __name__ == "__main__":
    now = 1993

    ginny = Pupil.ginny()
    print(ginny.says("Be careful Neville!"))

