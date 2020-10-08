import datetime
from typing import NamedTuple

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

    @classmethod
    def mocking_knight(cls):
        return cls('The Mocking Knight', 1401, 'male', 1492)

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"birthyear={self.birthyear}, sex='{self.sex}', "
                f"year_of_death={self.year_of_death})")

class Pupil(CastleKilmereMember):
    """ Create a Castle Kilmere Pupil """
    def __init__(self, name: str, birthyear: int, sex: str, start_year: int, pet: tuple = None):
        super().__init__(name, birthyear, sex)
        self.start_year = start_year

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

class DarkArmyMember(NamedTuple):
    """ Creates a member of the Dark Army """
    name: str
    birthyear: str

    @property
    def leader(self):
        master_odon = DarkArmyMember('Master Odon', 1971)
        return master_odon

if __name__ == "__main__":
    keres = DarkArmyMember('Keres Fulford', 1953)
    print('Keres: ', keres)
    print('Leader: ', keres.leader)






