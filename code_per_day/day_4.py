"""
File: day_4.py
Author: Anna-Lena Popkes
Email: popkes@gmx.net
Github: https://github.com/zotroneneis
Description: all code for day 4 of my new coding habit
Link to blog post with explanations: http://www.alpopkes.com/posts/2018/07/coding-challenge-day-4/
"""

class CastleKilmereMember:
    """ Creates a member of the Castle Kilmere School of Magic """
    def __init__(self, name: str, birthyear: int, sex: str):
        self.name = name
        self.birthyear = birthyear
        self.sex = sex

    def says(self, words: str) -> str:
        return f"{self.name} says {words}"

    @classmethod
    def school_headmistress(cls) -> 'CastleKilmereMember':
        return cls('Miranda Mirren', 1963, 'female')

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"birthyear={self.birthyear}, sex='{self.sex}')")

class Pupil(CastleKilmereMember):
    """ Create a Castle Kilmere Pupil """
    def __init__(self, name: str, birthyear: int, sex: str, start_year: int, pet=None):
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

    @classmethod
    def luke(cls) -> 'Pupil':
        return cls('Luke Bery', 2008, 'male', 2018, ('Cotton', 'owl'))

    @classmethod
    def lissy(cls) -> 'Pupil':
        return cls('Lissy Spinster', 2008, 'female', 2018, ('Ramses', 'cat'))

    @classmethod
    def adrien(cls) -> 'Pupil':
        return cls('Adrien Fulford', 2008, 'male', 2018, ('Unnamed', 'owl') )

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"birthyear={self.birthyear}, sex='{self.sex}', "
                f"start_year={self.start_year})")

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

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"birthyear={self.birthyear}, sex='{self.sex}', "
                f"year_of_death={self.year_of_death})")

if __name__ == "__main__":
    bromley = CastleKilmereMember(name='Bromley Huckabee', birthyear=1959, sex='male')
    print('bromley: ', bromley)
    lissy = Pupil(name='Lissy Spinster', birthyear=2008, sex='female', start_year=2018)
    print('lissy: ', lissy)
    blade = Professor.blade()
    print('blade: ', blade)
