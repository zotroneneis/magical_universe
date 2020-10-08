import pytest
import datetime
from magical_universe import Professor

now = datetime.datetime.now().year

@pytest.fixture
def briddle():
    return Professor.briddle()

def test_correctness_of_attributes_(briddle):
    assert briddle.name == "Birdie Briddle"
    assert briddle.subject == "Foreign Magical Systems"
    assert briddle.department == "Department of Law"

def test_repr_output(capfd, briddle):
    print(briddle)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Professor(name='Birdie Briddle', birthyear=1931, sex='female', subject='Foreign Magical Systems', department='Department of Law')"
