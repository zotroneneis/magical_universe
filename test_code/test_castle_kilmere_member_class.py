import pytest
from magical_universe.magical_universe import CastleKilmereMember
import datetime

now = datetime.datetime.now().year

@pytest.fixture
def bromley():
    bromley = CastleKilmereMember('Bromley Huckabee', 1956, 'male')
    return bromley

@pytest.fixture
def bromley_with_traits():
    bromley = CastleKilmereMember('Bromley Huckabee', 1956, 'male')
    bromley.add_trait('kind')
    bromley.add_trait('wild')
    bromley.add_trait('mean', False)
    return bromley

def test_correctness_of_attributes_(bromley):
    assert bromley._name == 'Bromley Huckabee'
    assert bromley.birthyear == 1956
    assert bromley.sex == 'male'

def test_add_positive_traits(bromley):
    bromley.add_trait('kind')
    bromley.add_trait('wild')
    assert bromley._traits == {'kind': True, 'wild': True}

def test_add_negative_trait(bromley):
    bromley.add_trait('mean', False)
    assert bromley._traits == {'mean': False}

def test_exhibit_traits(bromley_with_traits):
    assert bromley_with_traits.exhibits_trait('kind') == True
    assert bromley_with_traits.exhibits_trait('mean') == False
    assert bromley_with_traits.exhibits_trait('smart') == None

def test_print_traits(capfd, bromley_with_traits):
    bromley_with_traits.print_traits()
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'Bromley Huckabee is kind, wild but not mean'

def test_init_raises_exception_with_missing_arguments():
    with pytest.raises(TypeError):
        bromley = CastleKilmereMember()

def test_says(bromley):
    assert bromley.says("Hi Cleon!") == "Bromley Huckabee says: Hi Cleon!"

def test_name_property(bromley):
    assert bromley.name == 'Bromley Huckabee'

def test_age_property(bromley):
    assert bromley.age == (now - bromley.birthyear) # this holds only if the current year is 2018!

def test_repr_output(capfd, bromley):
    print(bromley)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'CastleKilmereMember(Bromley Huckabee, birthyear: 1956)'

