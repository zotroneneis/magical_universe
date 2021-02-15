from collections import defaultdict

class CastleKilmereMember:
    """ Creates a member of the Castle Kilmere School of Magic """
    def __init__(self, name: str, birthyear: int, sex: str):
        self.name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = defaultdict(lambda: False)

    def add_trait(self, trait, value=True):
        self._traits[trait] = value

    def exhibits_trait(self, trait: str) -> bool:
        value = self._traits[trait]
        return value

    def print_traits(self):
        true_traits = [trait for trait, value in self._traits.items() if value]
        false_traits = [trait for trait, value in self._traits.items() if not value]

        if true_traits:
            print(f"{self.name} is {', '.join(true_traits)}")
        if false_traits:
            print(f"{self.name} is not {', '.join(false_traits)}")
        if (not true_traits and not false_traits):
            print(f"{self.name} does not have traits yet")

if __name__ == "__main__":

    bromley = CastleKilmereMember('Bromley Huckabee', 1959, 'male')

    bromley.add_trait('tidy-minded')
    bromley.add_trait('kind')

    bromley.exhibits_trait('kind')
    bromley.exhibits_trait('mean')

    bromley.print_traits()
    
