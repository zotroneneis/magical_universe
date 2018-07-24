import datetime
import ipdb

class HogwartsMember:

    def __init__(self, name:str, birthyear:int):
        self._name = name
        self.birthyear = birthyear

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    @staticmethod
    def school_headmaster():
        return HogwartsMember('Albus Percival Wulfric Brian Dumbledore', 1881)

class Pupil(HogwartsMember):

    def __init__(self, name:str, birthyear:int, house:str, start_year:int):
        super(Pupil, self).__init__(name, birthyear)
        self.house = house
        self.start_year = start_year
        self._owls = {'Study of Ancient Runes': False, 'Arithmancy': False, 'Astronomy': False, 'Care of Magical Creatures': False, 'Charms': False, 'Defence Against the Dark Arts': False, 'Divination': False, 'Herbology': False, 'History of Magic': False, 'Muggle Studies': False, 'Potions': False, 'Transfiguration': False}

    @property
    def current_year(self):
        now = datetime.datetime.now().year
        return (now - self.start_year) + 1
   
    @property
    def owls(self):
        return self._owls

    @owls.setter
    def owls(self, subject_and_grade):

        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError("Pass and iterable with two items: subject and grade")

        passed = self.passed(grade)

        if not passed:
            raise ValueError('The exam was not passed so no OWL was awarded!')

        self._owls[subject] = True

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
                'Dreadful': False,
                'T': False,
                'Troll': False,
                }

        return grades.get(grade, False)
    

if __name__ == "__main__":
    now = 1995

    hagrid = HogwartsMember(name='Rubeus Hagrid', birthyear=1928)
    print(hagrid.age)
    print(hagrid.name)

    harry = Pupil(name='Harry James Potter', birthyear=1980, house='Griffindor', start_year=1991)
    print(harry.owls)
    harry.owls = ('Defence Against the Dark Arts', 'O')

    headmaster = harry.school_headmaster()
    print(headmaster.name)

