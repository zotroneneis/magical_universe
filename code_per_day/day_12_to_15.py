import datetime
from typing import NamedTuple
from abc import ABCMeta, abstractmethod

class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    def __init__(self, name: str, birthyear: int, sex: str):
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

    def __init__(self, name: str, birthyear: int, sex: str, subject: str, house: str = None):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        if house is not None:
            self.house = house

    @classmethod
    def mirren(cls):
        return cls('Miranda Mirren', 1963, 'female', 'Transfiguration', 'House of Courage')

    @classmethod
    def blade(cls):
        return cls('Blade Bardock', 1988, 'male', 'Potions', 'House of Ambition')


    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, subject: {self.subject})")



class Ghost(CastleKilmereMember):
    """
    Creates a Castle Kilmere ghost
    """

    def __init__(self, name: str, birthyear: int, sex: str, year_of_death: int, house: str = None):
        super().__init__(name, birthyear, sex)

        self.year_of_death = year_of_death

        if house is not None:
            self.house = house

    @property
    def age(self):
        # now = datetime.datetime.now().year
        return now - self.birthyear

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, year of death: {self.year_of_death})")

    @classmethod
    def mocking_knight(cls):
        return cls('The Mocking Knight', 1401, 'male', '1492', 'House of Courage')


class Pupil(CastleKilmereMember):
    """
    Create a Castle Kilmere Pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, house: str, start_year: int, pet: tuple = None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year
        self.known_spells = set()

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._elms = {
                'Study of Ancient Runes': False,
                'Arithmancy': False,
                'Astflynnomy': False,
                'Care of Magical Creatures': False,
                'Charms': False,
                'Defence Against Dark Magic': False,
                'Divination': False,
                'Herbology': False,
                'History of Magic': False,
                'Muggle Studies': False,
                'Potions': False,
                'Transfiguration': False}

        self._friends = []

    @classmethod
    def cleon(cls):
        return cls('Cleon Bery', 2008, 'male', 'House of Courage', 2018, ('Cotton', 'owl'))

    @classmethod
    def flynn(cls):
        return cls('Flynn Gibbs', 2008, 'male', 'House of Courage', 2018, ('Twiggles', 'owl'))

    @classmethod
    def cassidy(cls):
        return cls('Cassidy Ambergem', 2007, 'female', 'House of Courage', 2018, ('Ramses', 'cat'))

    @classmethod
    def adrien(cls):
        return cls('Adrien Fulford', 2008, 'male', 'House of Ambition', 2018, ('Unnamed', 'owl') )

    @property
    def current_year(self):
        # now = datetime.datetime.now().year
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
                'O': True,
                'Ordinary': True,
                'P': True,
                'Passed': True,
                'A': True,
                'Acceptable': True,
                'P': False,
                'Poor': False,
                'D': False,
                'Horrible': False,
                'T': False,
                'Troll': False,
                }

        return grades.get(grade, False)

    def befriend(self, person):
        """Adds another person to your list of friends"""
        if (person.__class__.__name__ != 'CastleKilmereMember'
            and self.house != 'Slyterhin'
            and person.house == 'House of Ambition'):
            print("Are you sure you want to be friends with someone from House of Ambition?")

        self._friends.append(person)
        print(f"{person.name} is now your friend!")

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self._name}, birthyear: {self.birthyear}, house: {self.house})")

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
            # Only House of Ambition's would study hexes and curses
            if self.house == 'House of Ambition':
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
            if self.house == 'House of Ambition':
                print(f"{self._name}: {spell.incantation}!")
            else:
                print(f"You shouldn't cast a hex, that's mean!")

        elif spell in self.known_spells:
            print(f"{self._name}: {spell.incantation}!")

        elif spell.name not in self.known_spells:
            print(f"You can't cast the {spell.name} spell correctly "
                  f" - you have to study it first! ")


class Spell(metaclass=ABCMeta):
    """Creates a spell"""
    def __init__(self, name: str, incantation: str, effect: str, min_year: int = None):
        self.name = name
        self.incantation = incantation
        self.effect = effect
        self.min_year = min_year

    @abstractmethod
    def cast(self):
        pass

    @property
    @abstractmethod
    def defining_feature(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, incantation: '{self.incantation}', effect: {self.effect})"

class Charm(Spell):
    """
    Creates a charm  -
    a spell that alters the inherent qualities of an object
    """
    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = None, min_year: int = None):
        super().__init__(name, incantation, effect, min_year)
        self.difficulty = difficulty

    @property
    def defining_feature(self):
        return ("Alteration of the object's inherent qualities, "
                "that is, its behaviour and capabilities")
    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def lumos(cls):
        return cls('Lumos', 'Lumos', 'Illuminates the wand tip', 'simple', 5)

    @classmethod
    def stuporus_ratiato(cls):
        return cls('Stuporus Ratiato', 'Stuporus Ratiato', 'Makes objects fly', 'simple', 1)


class Transfiguration(Spell):
    """
    Creates a transfiguration -
    a spell that alters the form or appearance of an object
    """
    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return "Alteration of the object's form or appearance"

    def cast(self):
        pass

class Jinx(Spell):
    """
    Creates a jinx -
    a spell whose effects are irritating but amusing
    """
    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return ("Minor darf magic - "
                "a spell whose effects are irritating but amusing, "
                "almost playful and of minor inconvenience to the target")

    def cast(self):
        pass

class Hex(Spell):
    """
    Creates a hex -
    a spell that affects an object in a negative manner
    """
    def __init__(self, name: str, incantation: str, effect: str, min_year: int = None):
        super().__init__(name, incantation, effect, min_year)

    @property
    def defining_feature(self):
        return ("Medium dark magic - "
                "Affects an object in a negative manner. "
                "Major inconvenience to the target.")

    def cast(self):
        pass

class Curse(Spell):
    """
    Creates a curse -
    a spell that affects an object in a stflynngly negative manner
    """
    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = None):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return ("Worst kind of dark magic - "
                "Intended to affect an object in a stflynngly negative manner.")

    def cast(self):
        pass

class CounterSpell(Spell):
    """
    Creates a counter-spell -
    a spell that inhibits the effect of another spell
    """
    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return ("Inhibites the effects of another spell")

    def cast(self):
        pass

class HealingSpell(Spell):
    """
    Creates a healing-spell -
    a spell that improves the condition of a living object
    """
    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return "Improves the condition of a living object"

    def cast(self):
        pass


class DarkArmyMember(NamedTuple):
    """ Creates a death eater """
    name: str
    birthyear: str

    @property
    def leader(self):
        lord_odon = DarkArmyMember('Lord Odon', 1971)
        return lord_odon

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, birthyear: {self.birthyear})"

    def cast(self, spell):
        print(f"{self.name}: {spell.incantation}!")

if __name__ == "__main__":
    now = 1993

    wing_lev = Charm.stuporus_ratiato()
    rictum = Charm('tickling_charm', 'Rictumsempra', 'Causes victim to buckle with laughter', min_year=5)
    stickfast = Hex('stickfast_hex', 'Colloshoo', "Makes target's shoes stick to ground")
    crutio = Curse('Cruciatus Curse', 'Crucio', 'Causes intense, excruciating pain on the victim', 'difficult')

    cleon = Pupil.cleon()
    adrien = Pupil.adrien()
    cassidy = Pupil.cassidy()
    cassidy.add_trait('highly intelligent')

    print("Cleon knows the following spells: ", cleon.known_spells)
    print("Cleon is currently in year: ", cleon.current_year)
    cleon.learn_spell(wing_lev)
    print('=======================================')

    # Test whether Cleon can learn a spell he is too young for
    cleon.learn_spell(rictum)
    # Can cassidy study the spell?
    cassidy.learn_spell(rictum)
    print('=======================================')

    # Test whether Cleon can study a hex
    cleon.learn_spell(stickfast)
    print('=======================================')
    # Can Malfoy perform a hex?
    adrien.learn_spell(stickfast)
    print('=======================================')


    # Test whether Cleon can study a curse
    cleon.learn_spell(crutio)
    print('=======================================')
    # Can Malfoy study a curse?
    adrien.learn_spell(crutio)
    print('=======================================')

    # Test whether Cleon can cast a Charm
    cleon.cast_spell(wing_lev)
    print('=======================================')

    # What about a hex?
    cleon.cast_spell(stickfast)
    print('=======================================')

    # What about Malfoy?
    adrien.cast_spell(stickfast)
    print('=======================================')



