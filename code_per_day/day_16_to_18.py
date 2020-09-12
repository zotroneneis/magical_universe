import datetime
from typing import NamedTuple
from dataclasses import dataclass

class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    def __init__(self, name:str, birthyear:int, sex:str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}

    def says(self, words):
        return f"{self._name} says {words}"

    def add_trait(self, trait, value=True):
        self._traits[trait] = value

    def print_traits(self):
        true_traits = [trait for trait, value in self._traits.items() if value]
        false_traits = [trait for trait, value in self._traits.items() if not value]

        if true_traits:
            print(f"{self._name} is {', '.join(true_traits)}")
        if false_traits:
            print(f"{self._name} is not {', '.join(false_traits)}")
        if (not true_traits and not false_traits):
            print(f"{self._name} does not have traits yet")

    def exhibits_trait(self, trait):
        try:
            value = self._traits[trait]
        except KeyError:
            return False
        return value

        return value

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    @staticmethod
    def school_headmaster():
        return CastleKilmereMember('Miranda Mirren', 1963, 'female')

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})"


class Professor(CastleKilmereMember):
    """
    Creates a Castle Kilmere professor
    """
    def __init__(self, name: str, birthyear: int, sex: str, subject: str, department: str = None):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        self.department = department

    @classmethod
    def blade(cls):
        return cls('Blade Bardock', 1988, 'male', 'Potions', 'Science')

    @classmethod
    def briddle(cls):
        return cls('Birdie Briddle', 1931, 'female', 'Foreign Magical Systems', 'Law')

    @classmethod
    def radford(cls):
        return cls('Rupert Radford', 1900, 'male', 'Illusions 101')

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, subject: {self.subject})")



class Ghost(CastleKilmereMember):
    """
    Creates a Castle Kilmere ghost
    """

    def __init__(self, name:str, birthyear:int, sex:str, year_of_death:int):
        super().__init__(name, birthyear, sex)

        self.year_of_death = year_of_death

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, year of death: {self.year_of_death})")

    @classmethod
    def mocking_knight(cls):
        return cls('The Mocking Knight', 1401, 'male', 1492)

    @classmethod
    def gray_groom(cls):
        return cls('The Gray Groom', 1000, 'male', 1050)

    @classmethod
    def scary_scoundrel(cls):
        return cls('Scary Scoundrel', 983, 'male', 1010)

    @classmethod
    def old_lady(cls):
        return cls('The Old Lady', 983, 'male', 996)


@dataclass
class Department:
    """ Creates a Castle Kilmere Department """
    name: str
    head: Professor
    founded_in: int = 991

    def current_age(self):
        now = datetime.datetime.now().year
        return (now - self.founded_in) + 1


if __name__ == "__main__":
    mocking_knight = Ghost.mocking_knight()
    gray_groom = Ghost.gray_groom()
    scary_scoundrel = Ghost.scary_scoundrel()
    old_lady = Ghost.old_lady()

    briddle = Professor.briddle()
    blade = Professor.blade()
    radford = Professor.radford()
    print('Age of Professor Radford: ', radford.age)


    law_department = Department('Law',
                       briddle,
                       mocking_knight)
    print('law_department: ', law_department)

    science_department = Department('Science', blade, scary_scoundrel)
    print('science_department: ', science_department)

    arts_department = Department('Creativity and Arts', radford, old_lady)
    print('arts_department: ', arts_department)


