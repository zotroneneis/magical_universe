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

        print(f"{self._name} is {', '.join(true_traits)} "
              f"but not {', '.join(false_traits)}")

    def exhibits_trait(self, trait):
        try:
            value = self._traits[trait]
        except KeyError:
            print(f"{self._name} does not have a character trait with the name '{trait}'")
            return

        if value:
            print(f"Yes, {self._name} is {trait}!")
        else:
            print(f"No, {self._name} is not {trait}!")

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
        return CastleKilmereMember('Redmond Dalodore', 1939, 'male')

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})"


class Professor(CastleKilmereMember):
    """
    Creates a Castle Kilmere professor
    """

    def __init__(self, name:str, birthyear:int, sex:str, subject:str, house: str = None):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        self.house = house

    @classmethod
    def mirren(cls):
        return cls('Miranda Mirren', 1963, 'female', 'Transfiguration', 'House of Courage')

    @classmethod
    def blade(cls):
        return cls('Blade Bardock', 1988, 'male', 'Potions', 'House of Ambition')

    @classmethod
    def briddle(cls):
        return cls('Birdie Briddle', 1931, 'female', 'Herbology', 'House of Loyalty')

    @classmethod
    def radford(cls):
        return cls('Rupert Radford', 1900, 'male', 'Charms', 'House of Wisdom')

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, subject: {self.subject})")



class Ghost(CastleKilmereMember):
    """
    Creates a Castle Kilmere ghost
    """

    def __init__(self, name:str, birthyear:int, sex:str, year_of_death:int, house: str = None):
        super().__init__(name, birthyear, sex)

        self.year_of_death = year_of_death
        self.house = house

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, year of death: {self.year_of_death})")

    @classmethod
    def mocking_knight(cls):
        return cls('The Mocking Knight', 1401, 'male', 1492, 'House of Courage')

    @classmethod
    def gray_groom(cls):
        return cls('The Gray Groom', 1000, 'male', 1050, 'House of Loyalty')

    @classmethod
    def scary_scoundrel(cls):
        return cls('Scary Scoundrel', 983, 'male', 1010, 'House of Ambition')

    @classmethod
    def old_lady(cls):
        return cls('The Old Lady', 983, 'male', 996, 'House of Wisdom')


@dataclass
class House:
    """ Creates a Castle Kilmere House """
    name: str
    traits: list
    head: Professor
    ghost: Ghost
    founded_in: int = 991

    def current_age(self):
        now = datetime.datetime.now().year
        return (now - self.founded_in) + 1


if __name__ == "__main__":
    mocking_knight = Ghost.mocking_knight()
    gray_groom = Ghost.gray_groom()
    scary_scoundrel = Ghost.scary_scoundrel()
    old_lady = Ghost.old_lady()

    mirren = Professor.mirren()
    briddle = Professor.briddle()
    blade = Professor.blade()
    radford = Professor.radford()
    print('Age of Professor Radford: ', radford.age)


    house_of_courage = House('House of Courage',
                       ['bravery', 'nerve', 'courage'],
                       mirren,
                       mocking_knight)
    print('house_of_courage: ', house_of_courage)

    house_of_loyalty = House('House of Loyalty',
                       ['loyalty', 'fairness', 'patience', 'kindness'],
                       briddle,
                       gray_groom)
    print('house_of_loyalty: ', house_of_loyalty)

    house_of_ambition = House('House of Ambition',
                      ['cunning', 'ambition', 'determination'],
                      blade,
                      scary_scoundrel)
    print('house_of_ambition: ', house_of_ambition)

    house_of_wisdom = House('House of Wisdom',
                      ['intelligence', 'wit', 'wisdom'],
                      radford,
                      old_lady)
    print('house_of_wisdom: ', house_of_wisdom)


