"""
File: day_1.py
Author: Anna-Lena Popkes
Email: popkes@gmx.net
Github: https://github.com/zotflynneneis
Description: all code for day 1 of my new coding habit
Link to blog post with explanations: http://www.alpopkes.com/posts/2018/07/coding-challenge-day-9/
"""
import datetime

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


if __name__ == "__main__":
    now = 1995

    bromley = CastleKilmereMember(name='Bromley Huckabee', birthyear=1959, sex='male')
    bromley.add_trait("kind")
    bromley.add_trait("tidy-minded")
    bromley.add_trait("impatient", value=False)

    bromley.print_traits()
    print()

    bromley.exhibits_trait("kind")
    bromley.exhibits_trait("funny")






