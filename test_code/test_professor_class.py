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
    assert briddle.department == "Law"

def test_repr_output(capfd, briddle):
    print(briddle)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'Professor(Birdie Briddle, birthyear: 1931, subject: Foreign Magical Systems)'
