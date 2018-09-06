import functools

class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}

    def whisper(function):
        @functools.wraps(function)
        def wrapper(self, *args):
            ''' Whispering decorator '''
            original_output = function(self, *args)
            first_part, words = original_output.split(' says: ')
            words = words.replace('!', '.')
            new_output = f"{first_part} whispers: {words}.."
            return new_output
        return wrapper

    @whisper
    def says(self, words):
        '''Allows a Castle Kilmere Member to talk'''
        return f"{self._name} says: {words}"


if __name__ == "__main__":
    bromley = CastleKilmereMember('Bromley Huckabee', 1959, 'male')

    print(bromley.says.__name__)
    print(bromley.says.__doc__)
