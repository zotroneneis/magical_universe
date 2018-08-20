class Potion:
    """ Creates a potion """
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1

        if self.counter == len(self.ingredients):
            raise StopIteration

        return self.ingredients[self.counter]


if __name__ == "__main__":

    flask_of_remembrance = Potion(['raven eggshells', 'tincture of thyme', 'unicorn tears',
                                    'dried onions', 'powdered ginger root'])

    vial_of_anger = Potion(['dried dragon skin', 'leeches', 'shredded elephant tusk',
                            'horned flies', 'earthworm juice'])

    for ingredient in flask_of_remembrance:
        print(ingredient)



