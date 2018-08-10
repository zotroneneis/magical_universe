import datetime
from typing import NamedTuple
from dataclasses import dataclass

class HogwartsMember:
    """
    Creates a member of the Hogwarts School of Witchcraft and Wizardry
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
        return HogwartsMember('Albus Percival Wulfric Brian Dumbledore', 1881, 'male')

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})"


class Professor(HogwartsMember):
    """
    Creates a Hogwarts professor
    """

    def __init__(self, name:str, birthyear:int, sex:str, subject:str, house: str = None):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        self.house = house

    @classmethod
    def mcgonagall(cls):
        return cls('Minerva McGonagall', 1935, 'female', 'Transfiguration', 'Griffindor')

    @classmethod
    def snape(cls):
        return cls('Severus Snape', 1960, 'male', 'Potions', 'Slytherin')

    @classmethod
    def sprout(cls):
        return cls('Pomona Sprout', 1931, 'female', 'Herbology', 'Hufflepuff')

    @classmethod
    def flitwick(cls):
        return cls('Filius Flitwick', 1900, 'male', 'Charms', 'Ravenclaw')

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, subject: {self.subject})")



class Ghost(HogwartsMember):
    """
    Creates a Hogwarts ghost
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
    def nearly_headless_nick(cls):
        return cls('Sir Nicholas de Mimsy-Porpington', 1401, 'male', 1492, 'Gryffindor')

    @classmethod
    def fat_friar(cls):
        return cls('Fat Friar', 1000, 'male', 1050, 'Hufflepuff')

    @classmethod
    def bloody_baron(cls):
        return cls('Bloody Baron', 983, 'male', 1010, 'Slytherin')

    @classmethod
    def grey_lady(cls):
        return cls('Helena Ravenclaw', 983, 'male', 996, 'Ravenclaw')


@dataclass
class House:
    """ Creates a Hogwarts House """
    name: str
    founder: str
    traits: list
    common_room: str
    head: Professor
    ghost: Ghost
    founded_in: int = 991

    def current_age(self):
        now = datetime.datetime.now().year
        return (now - self.founded_in) + 1


if __name__ == "__main__":
    headless_nick = Ghost.nearly_headless_nick()
    fat_friar = Ghost.fat_friar()
    bloody_baron = Ghost.bloody_baron()
    grey_lady = Ghost.grey_lady()

    mcgonagall = Professor.mcgonagall()
    sprout = Professor.sprout()
    snape = Professor.snape()
    flitwick = Professor.flitwick()
    print('Age of professor Flitwick: ', flitwick.age)


    gryffindor = House('Gryffindor',
                       'Godric Gryffindor',
                       ['bravery', 'nerve', 'courage', 'chivalry', 'daring'],
                       'Gryffindor Tower',
                       mcgonagall,
                       headless_nick)

    hufflepuff = House('Hufflepuff',
                       'Helga Hufflepuff',
                       ['dedication', 'hardworking', 'fairness',
                           'patience', 'kindness', 'tolerance', 'loyalty'],
                       'Hufflepuff basement',
                       sprout,
                       fat_friar)

    slytherin = House('Slytherin',
                      'Salazar Slytherin',
                      ['cunning', 'ambition', 'determination', 'cleverness',
                          'resourcefulness', 'fraternity'],
                      'Slytherin dungeon',
                      snape,
                      bloody_baron)

    ravenclaw = House('Ravenclaw',
                      'Rowena Ravenclaw',
                      ['intelligence', 'wit', 'wisdom', 'creativity', 'acceptance', 'indiviuality'],
                      'Ravenclaw Tower',
                      flitwick,
                      grey_lady)


