from collections import defaultdict

class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = defaultdict(lambda: False)

    def add_trait(self, trait, value=True):
        self._traits[trait] = value

    def exhibits_trait(self, trait):
        value = self._traits[trait]

        if value:
            print(f"Yes, {self._name} is {trait}!")
        else:
            print(f"No, {self._name} is not {trait}!")

        return value

if __name__ == "__main__":

    bromley = CastleKilmereMember('Bromley Huckabee', '1959', 'male')

    bromley.add_trait('tidy-minded')
    bromley.add_trait('kind')

    bromley.exhibits_trait('kind')
    bromley.exhibits_trait('mean')

