import pytest
from magical_universe import Ghost
import datetime

now = datetime.datetime.now().year

@pytest.fixture
def mocking_knight():
    return Ghost.mocking_knight()

def test_correctness_of_attributes_(mocking_knight):
    assert mocking_knight.name == "The Mocking Knight"
    assert mocking_knight.year_of_death == 1492

def test_age_property(mocking_knight):
    assert mocking_knight.age == (now - mocking_knight.birthyear)

def test_repr_output(capfd, mocking_knight):
    print(mocking_knight)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'Ghost(The Mocking Knight, birthyear: 1401, year of death: 1492)'
