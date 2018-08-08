"""
File: day_1.py
Author: Anna-Lena Popkes
Email: popkes@gmx.net
Github: https://github.com/zotroneneis
Description: all code for day 1 of my new coding habit
Link to blog post with explanations: http://www.alpopkes.com/posts/2018/07/coding-challenge-day-1/
"""

class HogwartsMember:
    """
    Creates a member of the Hogwarts School of Witchcraft and Wizardry
    """

    def __init__(self, name, birthyear, sex):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex

    def says(self, words):
        return f"{self._name} says {words}"


class Pupil(HogwartsMember):
    """
    Create a Hogwarts Pupil
    """

    def __init__(self, name, birthyear, sex, house, start_year, pet=None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._owls = {
                'Study of Ancient Runes': False,
                'Arithmancy': False,
                'Astronomy': False,
                'Care of Magical Creatures': False,
                'Charms': False,
                'Defence Against the Dark Arts': False,
                'Divination': False,
                'Herbology': False,
                'History of Magic': False,
                'Muggle Studies': False,
                'Potions': False,
                'Transfiguration': False}

class Professor(HogwartsMember):
  """
  Creates a Hogwarts professor
  """

  def __init__(self, name, birthyear, sex, subject, house=None):
      super().__init__(name, birthyear, sex)
      self.subject = subject
      if house is not None:
          self.house = house


class Ghost(HogwartsMember):
    """
    Creates a Hogwarts ghost
    """

    def __init__(self, name, birthyear, sex, year_of_death, house=None):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

        if house is not None:
            self.house = house



if __name__ == "__main__":
  hagrid = HogwartsMember('Rubeus Hagrid', '1928', 'male')
  print(hagrid.says("Hello!"))

  harry = Pupil(name='Harry James Potter',
                birthyear=1980,
                sex='male',
                house='Gryffindor',
                start_year=1991,
                pet=('Hedwig', 'owl'))
