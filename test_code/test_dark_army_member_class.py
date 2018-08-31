import pytest
from magical_universe.magical_universe import DarkArmyMember, Charm

@pytest.fixture
def keres_fulford():
    keres_fulford = DarkArmyMember("Keres Fulford", 1953)
    return keres_fulford

@pytest.fixture
def lord_odon():
    lord_odon = DarkArmyMember('Lord Odon', 1971)
    return lord_odon

@pytest.fixture
def stuporus_ratiato():
    return Charm.stuporus_ratiato()

def test_correctness_of_attributes(keres_fulford):
    assert keres_fulford.name == "Keres Fulford"
    assert keres_fulford.birthyear == 1953

def test_leader_property(keres_fulford, lord_odon):
    assert keres_fulford.leader == lord_odon

def test_repr_output(capfd, keres_fulford):
    print(keres_fulford)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "DarkArmyMember(name='Keres Fulford', birthyear=1953)"

def test_cast_spell(keres_fulford, stuporus_ratiato):
    assert keres_fulford.cast_spell(stuporus_ratiato) == "Keres Fulford: Stuporus Ratiato!"
