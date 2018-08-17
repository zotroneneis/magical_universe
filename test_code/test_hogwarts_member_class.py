import pytest
from harry_potter_universe.harry_potter_universe import HogwartsMember

@pytest.fixture
def hagrid():
    hagrid = HogwartsMember('Rubeus Hagrid', 1928, 'male')
    return hagrid

@pytest.fixture
def hagrid_with_traits():
    hagrid = HogwartsMember('Rubeus Hagrid', 1928, 'male')
    hagrid.add_trait('kind')
    hagrid.add_trait('wild')
    hagrid.add_trait('mean', False)
    return hagrid

def test_correctness_of_attributes_(hagrid):
    assert hagrid._name == 'Rubeus Hagrid'
    assert hagrid.birthyear == 1928
    assert hagrid.sex == 'male'

def test_add_positive_traits(hagrid):
    hagrid.add_trait('kind')
    hagrid.add_trait('wild')
    assert hagrid._traits == {'kind': True, 'wild': True}

def test_add_negative_trait(hagrid):
    hagrid.add_trait('mean', False)
    assert hagrid._traits == {'mean': False}

def test_exhibit_traits(hagrid_with_traits):
    assert hagrid_with_traits.exhibits_trait('kind') == True
    assert hagrid_with_traits.exhibits_trait('mean') == False
    assert hagrid_with_traits.exhibits_trait('smart') == None

def test_print_traits(capfd, hagrid_with_traits):
    hagrid_with_traits.print_traits()
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'Rubeus Hagrid is kind, wild but not mean'

def test_init_raises_exception_with_missing_arguments():
    with pytest.raises(TypeError):
        hagrid = HogwartsMember()

def test_says(hagrid):
    assert hagrid.says("Hi Harry!") == "Rubeus Hagrid says: Hi Harry!"

def test_name_property(hagrid):
    assert hagrid.name == 'Rubeus Hagrid'

def test_age_property(hagrid):
    assert hagrid.age == 90 # this holds only if the current year is 2018!

def test_repr_output(capfd, hagrid):
    print(hagrid)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'HogwartsMember(Rubeus Hagrid, birthyear: 1928)'

