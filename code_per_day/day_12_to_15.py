import datetime
from typing import NamedTuple
from abc import ABC, abstractmethod

class CastleKilmereMember:
    """ Creates a member of the Castle Kilmere School of Magic """

    def __init__(self, name: str, birthyear: int, sex: str):
        self.name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}

    def says(self, words: str) -> str:
        return f"{self.name} says {words}"

    def add_trait(self, trait, value=True):
        self._traits[trait] = value

    def print_traits(self):
        true_traits = [trait for trait, value in self._traits.items() if value]
        false_traits = [trait for trait, value in self._traits.items() if not value]

        if true_traits:
            print(f"{self.name} is {', '.join(true_traits)}")
        if false_traits:
            print(f"{self.name} is not {', '.join(false_traits)}")
        if (not true_traits and not false_traits):
            print(f"{self.name} does not have traits yet")

    def exhibits_trait(self, trait: str) -> bool:
        try:
            value = self._traits[trait]
            return value
        except KeyError as e:
            print(f"{self.name} does not have a character trait with the name {e}")
            return False

    @property
    def age(self) -> int:
        now = datetime.datetime.now().year
        return now - self.birthyear

    @classmethod
    def school_headmistress(cls) -> 'CastleKilmereMember':
        return cls('Miranda Mirren', 1963, 'female')

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"birthyear={self.birthyear}, sex='{self.sex}')")


class Professor(CastleKilmereMember):
    """ Creates a Castle Kilmere professor """
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

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"birthyear={self.birthyear}, sex='{self.sex}', "
                f"subject='{self.subject}', department='{self.department}')")


class Ghost(CastleKilmereMember):
    """ Creates a Castle Kilmere ghost """
    def __init__(self, name: str, birthyear: int, sex: str, year_of_death: int):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

    @property
    def age(self) -> int:
        now = datetime.datetime.now().year
        return now - self.birthyear

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"birthyear={self.birthyear}, sex='{self.sex}', "
                f"year_of_death={self.year_of_death})")

    @classmethod
    def mocking_knight(cls):
        return cls('The Mocking Knight', 1401, 'male', 1492)


class Pupil(CastleKilmereMember):
    """ Create a Castle Kilmere Pupil """
    def __init__(self, name: str, birthyear: int, sex: str, start_year: int, pet: tuple = None):
        super().__init__(name, birthyear, sex)
        self.start_year = start_year
        self.known_spells = set()

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._elms = {
                  'Critical Thinking': False,
                  'Self-Defense Against Fresh Fruit': False,
                  'Broomstick Flying': False,
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
        return cls('Adrien Fulford', 2008, 'male', 2018, ('Twiggles', 'owl') )

    @property
    def current_year(self) -> int:
        now = datetime.datetime.now().year
        return (now - self.start_year) + 1

    @property
    def elms(self):
        return self._elms

    @property
    def friends(self):
        return f"{self.name}'s current friends are: {[person.name for person in self._friends]}"

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
                'Excellent': True,
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

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"birthyear={self.birthyear}, sex='{self.sex}', "
                f"start_year={self.start_year})")

    def learn_spell(self, spell):
        """ Allows a pupil to learn a spell, given that he/she is old enough """
        if spell.min_year is not None:
            if self.current_year >= spell.min_year:
                print(f"{self.name} now knows spell {spell.name}")
                self.known_spells.add(spell)

            elif self.exhibits_trait('highly intelligent'):
                print(f"{self.name} now knows spell {spell.name}")
                self.known_spells.add(spell)

            elif self.current_year < spell.min_year:
                print(f"{self.name} is too young to study this spell!")

        elif spell.__class__.__name__ in ['Hex', 'Curse']:
            # Only evil pupils would study hexes and curses
            if self.exhibits_trait('evil'):
                print(f"{self.name} now knows spell {spell.name}")
                self.known_spells.add(spell)

            else:
                print(f"How dare you study a hex or curse?!")

        else: 
            print(f"{self.name} now knows spell {spell.name}")
            self.known_spells.add(spell)

    def cast_spell(self, spell):
        """ Allows a pupil to cast a spell """
        if spell.__class__.__name__ == 'Curse':
            print("This is dark magic - stay away from performing curses!")

        elif spell.__class__.__name__ == 'Hex':
            if not self.exhibits_trait('evil'):
                print(f"You shouldn't cast a hex, that's mean!")

        elif spell in self.known_spells:
            print(f"{self.name}: {spell.incantation}!")

        elif spell.name not in self.known_spells:
            print(f"You can't cast the {spell.name} spell correctly "
                  f" - you have to study it first! ")


class Spell(ABC):
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
        return f"{self.__class__.__name__}(name='{self.name}', incantation='{self.incantation}', effect='{self.effect}', difficulty='{self.difficulty}', min_year={self.min_year})"


class Charm(Spell):
    """ Creates a charm  - a spell that alters the inherent qualities of an object """
    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = "Simple", min_year: int = 1):
        super().__init__(name, incantation, effect, min_year)
        self.difficulty = difficulty

    @property
    def defining_feature(self):
        return ("Alteration of the object's inherent qualities, "
                "that is, its behaviour and capabilities")

    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def stuporus_ratiato(cls):
        return cls('The Stuporus Ratiato charm', 'Stuporus Ratiato', 'Makes objects fly')


class Transfiguration(Spell):
    """ Creates a transfiguration - a spell that alters the form or appearance of an object """
    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return "Alteration of the object's form or appearance"

    def cast(self):
        pass

class Jinx(Spell):
    """ Creates a jinx - a spell whose effects are irritating but amusing """
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
    """ Creates a hex - a spell that affects an object in a negative manner """
    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return ("Medium dark magic - "
                "Affects an object in a negative manner. "
                "Major inconvenience to the target.")

    def cast(self):
        pass

class Curse(Spell):
    """ Creates a curse - a spell that affects an object in a stflynngly negative manner """
    def __init__(self, name: str, incantation: str, effect: str, difficulty):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return ("Worst kind of dark magic - "
                "Intended to affect an object in a stflynngly negative manner.")

    def cast(self):
        pass

class CounterSpell(Spell):
    """ Creates a counter-spell - a spell that inhibits the effect of another spell """
    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return ("Inhibites the effects of another spell")

    def cast(self):
        pass

class HealingSpell(Spell):
    """ Creates a healing-spell - a spell that improves the condition of a living object """
    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return "Improves the condition of a living object"

    def cast(self):
        pass


class DarkArmyMember(NamedTuple):
    """ Creates a member of the Dark Army """
    name: str
    birthyear: str

    @property
    def leader(self):
        master_odon = DarkArmyMember('Master Odon', 1971)
        return master_odon

    def cast(self, spell):
        print(f"{self.name}: {spell.incantation}!")

if __name__ == "__main__":

    ghost = Ghost.mocking_knight()
    print('ghost: ', ghost)
    print()

    stuporus = Charm.stuporus_ratiato()
    liberula = Charm('The liberula charm', 'Liberula', 'Allows a person to breathe under water', 'difficult', min_year=5)
    stickfast = Hex('The stickfast hex', 'Colloshoo', "Makes target's shoes stick to ground")
    fiera = Curse('Torture curse', 'Fiera Satanotis', 'Tortures a person, makes person suffer deeply', 'Difficult')

    lissy = Pupil.lissy()
    luke = Pupil.luke()
    lissy.print_traits()
    lissy.add_trait('highly intelligent')
    lissy.print_traits()

    adrien = Pupil.adrien()
    adrien.print_traits()
    adrien.add_trait('evil')
    adrien.print_traits()

    print("Lissy knows the following spells: ", lissy.known_spells)
    print("Lissy is currently in year: ", lissy.current_year)
    lissy.learn_spell(stuporus)
    print('=======================================')

    # Test whether lissy can learn a spell he is too young for
    luke.learn_spell(liberula)
    # Can cassidy study the spell?
    lissy.learn_spell(liberula)
    print('=======================================')

    # Test whether lissy can study a hex
    lissy.learn_spell(stickfast)
    print('=======================================')
    # Can Adrien perform a hex?
    adrien.learn_spell(stickfast)
    print('=======================================')


    # Test whether lissy can study a curse
    lissy.learn_spell(fiera)
    print('=======================================')
    # Can Adrien study a curse?
    adrien.learn_spell(fiera)
    print('=======================================')

    # Test whether lissy can cast a Charm
    lissy.cast_spell(stuporus)
    print('=======================================')

    # What about a hex?
    lissy.cast_spell(stickfast)
    print('=======================================')

    # What about Adrien?
    adrien.cast_spell(stickfast)
    print('=======================================')



