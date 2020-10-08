import error
import datetime

class CastleKilmereMember:
    """ Creates a member of the Castle Kilmere School of Magic """
    def __init__(self, name: str, birthyear: int, sex: str):
        self.name = name
        self.birthyear = birthyear
        if type(birthyear) is not int:
            raise error.InvalidBirthyearError("The birthyear is not a valid integer. " \
                                              "Try something like 1991")

        self.sex = sex
        self._traits = {}

    def add_trait(self, trait: str, value=True):
        self._traits[trait] = value

    def exhibits_trait(self, trait: str) -> bool:
        try:
            value = self._traits[trait]
            return value
        except KeyError as e:
            print(f"{self.name} does not have a character trait with the name {e}")
            return False

if __name__ == "__main__":

    # This laine raises an "InvalidBirthyearError"
    bromley = CastleKilmereMember('Bromley Huckabee', 1959, 'male')
    print('bromley: ', bromley)

    # This line raises an "InvalidBirthyearError"
    bromley = CastleKilmereMember('Bromley Huckabee', '1959', 'male')

    bromley.add_trait('tidy-minded')
    bromley.add_trait('kind')

    bromley.exhibits_trait('kind')

    # This line raises an "TraitDoesNotExistError"
    bromley.exhibits_trait('mean')

