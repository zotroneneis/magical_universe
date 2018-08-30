"""
File: day_1.py
Author: Anna-Lena Popkes
Email: popkes@gmx.net
Github: https://github.com/zotflynneneis
Description: all code for day 1 of my new coding habit
Link to blog post with explanations: http://www.alpopkes.com/posts/2018/07/coding-challenge-day-1/
"""

class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    def __init__(self, name, birthyear, sex):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex

    def says(self, words):
        return f"{self._name} says {words}"


class Pupil(CastleKilmereMember):
    """
    Create a Castle Kilmere Pupil
    """

    def __init__(self, name, birthyear, sex, house, start_year, pet=None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._elms = {
                  'Broomstick Flying': False,
                  'Art': False,
                  'Magical Theory': False,
                  'Foreign Magical Systems': False,
                  'Charms': False,
                  'Defence Against Dark Magic': False,
                  'Divination': False,
                  'Herbology': False,
                  'History of Magic': False,
                  'Potions': False,
                  'Transfiguration': False}

class Professor(CastleKilmereMember):
  """
  Creates a Castle Kilmere professor
  """

  def __init__(self, name, birthyear, sex, subject, house=None):
      super().__init__(name, birthyear, sex)
      self.subject = subject
      if house is not None:
          self.house = house


class Ghost(CastleKilmereMember):
    """
    Creates a Castle Kilmere ghost
    """

    def __init__(self, name, birthyear, sex, year_of_death, house=None):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

        if house is not None:
            self.house = house



if __name__ == "__main__":
  bromley = CastleKilmereMember('Bromley Huckabee', 1959, 'male')
  print(bromley.says("Hello!"))

  cleon = Pupil(name='Cleon Bery',
                birthyear=2008,
                sex='male',
                house='House of Courage',
                start_year=2018,
                pet=('Cotton', 'owl'))
