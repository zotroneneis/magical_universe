from collections import Counter
from magical_universe import Potion

# Step 1: Create the potions
flask_of_remembrance = Potion(['raven eggshells', 'tincture of thyme', 'unicorn tears',
                                'dried onions', 'powdered ginger root'])

vial_of_anger = Potion(['dried dragon skin', 'leeches', 'shredded elephant tusk',
                        'horned flies', 'earthworm juice', 'dried onions'])

ancient_wisdom = Potion(['tincture of thyme', 'leeches', 'drakus flower', 'lavender sprig',
                          'earthworm juice', 'cactus juice', 'dried onions'])

brew_of_lies = Potion(['horned flies', 'leeches', 'drakus flower', 'horned flies',
                        'unicorn tears', 'cactus juice'])

# Step 2: Create list of all potions
all_potions = [flask_of_remembrance, vial_of_anger, ancient_wisdom, brew_of_lies]

# Step 3: Create the shopping list!
shopping_list = Counter()

for potion in all_potions:
    for ingredient in potion:
        shopping_list[ingredient] += 1

print(f"Final shopping list: {shopping_list}")

