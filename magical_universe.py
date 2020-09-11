import datetime
import functools

from typing import NamedTuple
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from collections import defaultdict

class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = defaultdict(lambda: False)

    def write_letter(self, recipient, content):
        letter_name = f"dear_{recipient}.txt"
        with Letter(letter_name) as l:
            l.write(content)

    def whisper(function):
        @functools.wraps(function)
        def wrapper(self, *args):
            ''' Whispering decorator '''
            original_output = function(self, *args)
            first_part, words = original_output.split(' says: ')
            words = words.replace('!', '.')
            new_output = f"{first_part} whispers: {words}.."
            return new_output
        return wrapper

    def says(self, words):
        '''Allows a Castle Kilmere Member to talk'''
        return f"{self._name} says: {words}"

    def add_trait(self, trait, value=True):
        self._traits[trait] = value

    def print_traits(self):
        true_traits = [trait for trait, value in self._traits.items() if value]
        false_traits = [trait for trait, value in self._traits.items() if not value]

        print(f"{self._name} is {', '.join(true_traits)} "
              f"but not {', '.join(false_traits)}")

    def exhibits_trait(self, trait):
        value = self._traits[trait]

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
        return cls('Rupert Radford', 1958, 'male', 'Illusions 101', 'Creativity and Arts')

    @classmethod
    def giddings(cls):
        return cls('Gabriel Giddings', 1974, 'male', 'Broomstick Making', 'Engineering')

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, subject: {self.subject})")


class Ghost(CastleKilmereMember):
    """
    Creates a Castle Kilmere ghost
    """

    def __init__(self, name: str, birthyear: int, sex: str, year_of_death: int):
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

    @classmethod
    def boneless_barde(cls):
        return cls("The Boneless Bard", 1211, 'male', 1288)


class Pupil(CastleKilmereMember):
    """
    Create a Castle Kilmere Pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, start_year: int, pet: tuple = None):
        super().__init__(name, birthyear, sex)
        self.start_year = start_year
        self.known_spells = set()

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._elms = {
                  'Broomstick Flying': False,
                  'Art': False,
                  'Magical Theory': False,
                  'Foreign Magical Systems': False,
                  'Charms': False,
                  'Defence Against Dark Magic': False,
                  'History of Magic': False,
                  'Potions': False,
                  'Transfiguration': False}

        self._friends = []

    @classmethod
    def luke(cls):
        return cls('Luke Bery', 2008, 'male', 2018, ('Cotton', 'owl'))

    @classmethod
    def lissy(cls):
        return cls('Lissy Spinster', 2008, 'female', 2018, ('Ramses', 'cat'))

    @classmethod
    def adrien(cls):
        return cls('Adrien Fulford', 2008, 'male', 2018, ('Unnamed', 'owl') )

    @property
    def current_year(self):
        now = datetime.datetime.now().year
        return (now - self.start_year) + 1

    @property
    def elms(self):
        return self._elms

    @property
    def friends(self):
        return f"{self._name}'s current friends are: {[person.name for person in self._friends]}"

    @elms.setter
    def elms(self, subject_and_grade):

        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError("Pass and iterable with two items: subject and grade")

        passed = self.passed(grade)

        if passed:
            self._elms[subject] = True
        else:
            print('The exam was not passed so no ELM was awarded!')

    @elms.deleter
    def elms(self):
        print("Caution, you are deleting this students' ELM's! "
              "You should only do that if she/he dropped out of school without passing any exam!")
        del self._elms


    @staticmethod
    def passed(grade):
        """
        Given a grade, determine if an exam was passed.
        """
        grades = {
                'E': True,
                'Exceptional': True,
                'G': True,
                'Good': True,
                'A': True,
                'Acceptable': True,
                'P': False,
                'Poor': False,
                'H': False,
                'Horrible': False,
                }

        return grades.get(grade, False)

    def befriend(self, person):
        """Adds another person to your list of friends"""
        self._friends.append(person)
        print(f"{person.name} is now your friend!")

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self._name}, birthyear: {self.birthyear})")

    def learn_spell(self, spell):
        """
        Allows a pupil to learn a spell, given that he/she is old enough
        """
        if spell.min_year is not None:
            if self.current_year >= spell.min_year:
                print(f"{self._name} now knows spell {spell.name}")
                self.known_spells.add(spell)

            elif self.exhibits_trait('highly intelligent'):
                print(f"{self._name} now knows spell {spell.name}")
                self.known_spells.add(spell)

            elif self.current_year < spell.min_year:
                print(f"{self._name} is too young to study this spell!")

        elif spell.__class__.__name__ in ['Hex', 'Curse']:
            # Only evil pupils would study hexes and curses
            if self.exhibits_trait('evil'):
                print(f"{self._name} now knows spell {spell.name}")
                self.known_spells.add(spell)

            else:
                print(f"How dare you study a hex or curse?!")

    def cast_spell(self, spell):
        """
        Allows a pupil to cast a spell
        """
        if spell.__class__.__name__ == 'Curse':
            print("This is dark magic - stay away from performing curses!")

        elif spell.__class__.__name__ == 'Hex':
            if not self.exhibits_trait('evil'):
                print(f"You shouldn't cast a hex, that's mean!")

        elif spell in self.known_spells:
            return f"{self._name}: {spell.incantation}!"

        elif spell.name not in self.known_spells:
            print(f"You can't cast the {spell.name} spell correctly "
                  f" - you have to study it first! ")


class Spell(metaclass=ABCMeta):
    """Creates a spell"""
    def __init__(self, name: str, incantation: str, effect: str, difficulty: str, min_year: int = None):
        self.name = name
        self.incantation = incantation
        self.effect = effect
        self.difficulty = difficulty
        self.min_year = min_year

    @abstractmethod
    def cast(self):
        pass

    @property
    @abstractmethod
    def defining_feature(self):
        pass

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.name}, "
               f"incantation: '{self.incantation}', effect: {self.effect})")

class Charm(Spell):
    """
    Creates a charm  -
    a spell that alters the inherent qualities of an object
    """
    def __init__(self, name: str, incantation: str, effect: str,
                 difficulty: str, min_year: int = None):

        super().__init__(name, incantation, effect, difficulty, min_year)

    @property
    def defining_feature(self) -> str:
        return ("Alteration of the object's inherent qualities, "
                "that is, its behaviour and capabilities")

    def cast(self) -> str:
        return(f"{self.incantation}!")

    @classmethod
    def stuporus_ratiato(cls) -> 'Charm':
        return cls('Stuporus Ratiato', 'Stuporus Ratiato', 'Makes objects fly', 'simple', 1)

    @classmethod
    def liberula(cls) -> 'Charm':
        return cls('Liberula', 'Liberula', 'Allows a person to breath under water', 'difficult', 5)

class Transfiguration(Spell):
    """
    Creates a transfiguration -
    a spell that alters the form or appearance of an object
    """
    def __init__(self, name: str, incantation: str, effect: str,
                 difficulty: str, min_year: int = None):

        super().__init__(name, incantation, effect, difficulty, min_year)

    @property
    def defining_feature(self) -> str:
        return "Alteration of the object's form or appearance"

    @classmethod
    def alteraror_canieo(cls) -> 'Transfiguration':
        return cls('Alteraro Canieo', 'Alteraro Canieo', 'Turns an object into a can', 'simple', 2)

    def cast(self) -> str:
        return(f"{self.incantation}!")

class Jinx(Spell):
    """
    Creates a jinx -
    a spell whose effects are irritating but amusing
    """
    def __init__(self, name: str, incantation: str, effect: str,
                 difficulty: str, min_year: int = None):

        super().__init__(name, incantation, effect, difficulty, min_year)

    @property
    def defining_feature(self) -> str:
        return ("Minor darf magic - "
                "a spell whose effects are irritating but amusing, "
                "almost playful and of minor inconvenience to the target")

    @classmethod
    def inceptotis(cls) -> 'Jinx':
        return cls('Inceptotis', 'Inceptotis', 'Makes a person talk baby talk', 'simple')

    def cast(self) -> str:
        return(f"{self.incantation}!")

class Hex(Spell):
    """
    Creates a hex -
    a spell that affects an object in a negative manner
    """
    def __init__(self, name: str, incantation: str, effect: str,
                 difficulty: str, min_year: int = None):

        super().__init__(name, incantation, effect, difficulty, min_year)

    @property
    def defining_feature(self) -> str:
        return ("Medium dark magic - "
                "Affects an object in a negative manner. "
                "Major inconvenience to the target.")

    @classmethod
    def rectaro(cls) -> 'Hex':
        return cls('Rectaro', 'Rectaro', 'Exchanges a persons arms and legs', 'difficult')

    def cast(self) -> str:
        return(f"{self.incantation}!")

class Curse(Spell):
    """
    Creates a curse -
    a spell that affects an object in a stflynngly negative manner
    """
    def __init__(self, name: str, incantation: str, effect: str,
                 difficulty: str, min_year: int = None):

        super().__init__(name, incantation, effect, difficulty, min_year)

    @property
    def defining_feature(self) -> str:
        return ("Worst kind of dark magic - "
                "Intended to affect an object in a strongly negative manner.")

    @classmethod
    def fiera_satanotis(cls) -> 'Curse':
        return cls('Torture spell', 'Fiera Satanotis',
                   'Tortures a person, makes person suffer deeply', 'difficult')

    def cast(self) -> str:
        return(f"{self.incantation}!")

class CounterSpell(Spell):
    """
    Creates a counter-spell -
    a spell that inhibits the effect of another spell
    """
    def __init__(self, name: str, incantation: str, effect: str,
                 difficulty: str, min_year: int = None):

        super().__init__(name, incantation, effect, difficulty, min_year)

    @property
    def defining_feature(self) -> str:
        return ("Inhibites the effects of another spell")

    @classmethod
    def mufindo_immolim(cls) -> 'CounterSpell':
        return cls('Mufindo Immolim', 'Mufindo Immolim',
                   'Counteracts the immobilisation spell that prevents a person from moving', 'simple')

    def cast(self) -> str:
        return(f"{self.incantation}!")

class HealingSpell(Spell):
    """
    Creates a healing-spell -
    a spell that improves the condition of a living object
    """
    def __init__(self, name: str, incantation: str, effect: str,
                 difficulty: str, min_year: int = None):

        super().__init__(name, incantation, effect, difficulty, min_year)

    @property
    def defining_feature(self) -> str:
        return "Improves the condition of a living object"

    @classmethod
    def porim_perfite(cls) -> 'HealingSpell':
        return cls('Wound healing spell', 'Porim Perfite',
                   'Heals all kinds of wounds, even bad ones', 'difficult')

    def cast(self) -> str:
        return(f"{self.incantation}!")


@dataclass(frozen=True)
class DarkArmyMember():
    """ Creates a death eater """
    name: str
    birthyear: int

    @property
    def leader(self) -> 'DarkArmyMember':
        lord_odon = DarkArmyMember('Lord Odon', 1971)
        return lord_odon

    def cast_spell(self, spell) -> str:
        return(f"{self.name}: {spell.incantation}!")


@dataclass
class Department:
    """ Creates a Castle Kilmere Department """
    name: str
    traits: list
    head: Professor
    founded_in: int = 991

    def current_age(self):
        now = datetime.datetime.now().year
        return (now - self.founded_in) + 1


class Letter:
    total_number_of_letters = 0

    def __init__(self, letter_name):
        self.letter_name = letter_name
        self.__class__.total_number_of_letters += 1

    def __enter__(self):
        self.letter = open(self.letter_name, 'w')
        return self.letter

    def __exit__(self, exc_type, exc_value, traceback):
        if self.letter:
            self.letter.close()

class Potion:
    """ Creates a potion """
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1

        if self.counter == len(self.ingredients):
            raise StopIteration

        return self.ingredients[self.counter]


if __name__ == "__main__":
    bromley = CastleKilmereMember('Bromley Huckabee', 1959, 'male')

    print(bromley.says.__name__)
    print(bromley.says.__doc__)

    bromley.add_trait('tidy-minded')
    bromley.add_trait('kind')

    bromley.exhibits_trait('kind')
    bromley.exhibits_trait('mean')

