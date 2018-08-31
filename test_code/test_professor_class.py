import pytest
import datetime
from magical_universe import Professor

now = datetime.datetime.now().year

@pytest.fixture
def mirren():
    return Professor.mirren()

def test_correctness_of_attributes_(mirren):
    assert mirren.name == "Miranda Mirren"
    assert mirren.house == 'House of Courage'
    assert mirren.subject == 'Transfiguration'

def test_repr_output(capfd, mirren):
    print(mirren)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'Professor(Miranda Mirren, birthyear: 1963, subject: Transfiguration)'
