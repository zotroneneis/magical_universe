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
    """ Creates a member of the Castle Kilmere School of Magic """

    def __init__(self, name: str, birthyear: int, sex: str):
        self.name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}

    def says(self, words: str) -> str:
        return f"{self.name} says {words}"

    def add_trait(self, trait: str, value=True):
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


if __name__ == "__main__":
    bromley = CastleKilmereMember(name='Bromley Huckabee', birthyear=1959, sex='male')
    bromley.add_trait("kind")
    bromley.add_trait("tidy-minded")
    bromley.add_trait("impatient", value=False)

    bromley.print_traits()
    print()

    bromley.exhibits_trait("kind")
    bromley.exhibits_trait("funny")






