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

    @property
    def current_year(self):
        now = datetime.datetime.now().year
        return (now - self.start_year) + 1

if __name__ == "__main__":
    now = 1995

    hagrid = HogwartsMember(name='Rubeus Hagrid', birthyear=1928)
    print(hagrid.age)
    print(hagrid.name)

    harry = Pupil(name='Harry James Potter', birthyear=1980, house='Griffindor', start_year=1991)
    print(harry.age)
    print(harry.current_year)

    headmaster = harry.school_headmaster()
    print(headmaster.name)

