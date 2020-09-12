import pytest
from magical_universe import Potion

@pytest.fixture
def flask_of_remembrance():
    return Potion(['raven eggshells', 'tincture of thyme', 'unicorn tears',
                                    'dried onions', 'powdered ginger root'])
@pytest.fixture
def vial_of_anger():
    return Potion(['dried dragon skin', 'leeches', 'shredded elephant tusk',
                            'horned flies', 'earthworm juice'])

def test_iterator_behavior(flask_of_remembrance):
    all_ingredients = [ingredient for ingredient in flask_of_remembrance]
    assert all_ingredients == ['raven eggshells', 'tincture of thyme', 'unicorn tears',
                                    'dried onions', 'powdered ginger root']


