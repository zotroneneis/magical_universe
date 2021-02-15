import pytest
import datetime
from magical_universe import Pupil, Charm, Transfiguration, Hex, Curse, Jinx, HealingSpell, CounterSpell

now = datetime.datetime.now().year

@pytest.fixture
def stuporus_ratiato():
    return Charm.stuporus_ratiato()

@pytest.fixture
def liberula():
    return Charm.liberula()

@pytest.fixture
def alteraror_canieo():
    return Transfiguration.alteraror_canieo()

@pytest.fixture
def rectaro():
    return Hex.rectaro()

@pytest.fixture
def fiera_satanotis():
    return Curse.fiera_satanotis()

@pytest.fixture
def inceptotis():
    return Jinx.inceptotis()

@pytest.fixture
def porim_perfite():
    return HealingSpell.porim_perfite()

@pytest.fixture
def mufindo_immolim():
    return CounterSpell.mufindo_immolim()

@pytest.fixture
def luke():
    return Pupil.luke()

@pytest.fixture
def lissy():
    lissy = Pupil.lissy()
    lissy.add_trait('highly intelligent')
    return lissy

@pytest.fixture
def adrien():
    return Pupil.adrien()

@pytest.fixture
def luke_with_friends():
    luke = Pupil.luke()
    lissy = Pupil.lissy()
    luke.befriend(lissy)
    return luke

def test_correctness_of_attributes_(luke):
    assert luke.name == "Luke Bery"
    assert luke.start_year == 2020
    assert luke.pet_name == 'Cotton'
    assert luke.pet_type == 'owl'

def test_current_year_property(luke):
    assert luke.current_year == (now - luke.start_year + 1)

def test_elms_property(luke):
    assert luke._elms == {
                  'Critical Thinking': False,
                  'Self-Defense Against Fresh Fruit': False,
                  'Broomstick Flying': False,
                  'Magical Theory': False,
                  'Foreign Magical Systems': False,
                  'Charms': False,
                  'Defence Against Dark Magic': False,
                  'History of Magic': False,
                  'Potions': False,
                  'Transfiguration': False}

def test_friends_property(luke_with_friends):
    assert luke_with_friends.friends == "Luke Bery's current friends are: ['Lissy Spinster']"

def test_luke_befriend_lissy(capfd, luke, lissy):
    luke.befriend(lissy)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Lissy Spinster is now your friend!"

def test_befriend_house_adrien(capfd, luke, adrien):
    luke.befriend(adrien)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Adrien Fulford is now your friend!"

def test_delete_elms(capfd, luke):
    del luke.elms
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Caution, you are deleting this students' ELM's! You should only do that if she/he dropped out of school without passing any exam!"
    with pytest.raises(AttributeError):
        print(luke.elms)

def test_set_elms_raises_ValueError_with_wrong_input_argument(capfd, luke):
    with pytest.raises(ValueError):
        luke.elms = 'Transfiguration'

def test_set_elms_with_passed_grade(capfd, luke):
    luke.elms = ("Transfiguration", "G")
    assert luke._elms == {
                  'Critical Thinking': False,
                  'Self-Defense Against Fresh Fruit': False,
                  'Broomstick Flying': False,
                  'Magical Theory': False,
                  'Foreign Magical Systems': False,
                  'Charms': False,
                  'Defence Against Dark Magic': False,
                  'History of Magic': False,
                  'Potions': False,
                  'Transfiguration': True}

def test_set_elms_with_not_passed_grade(capfd, luke):
    luke.elms = ("Transfiguration", "H")
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'The exam was not passed so no ELM was awarded!'
    assert luke._elms == {
                  'Critical Thinking': False,
                  'Self-Defense Against Fresh Fruit': False,
                  'Broomstick Flying': False,
                  'Magical Theory': False,
                  'Foreign Magical Systems': False,
                  'Charms': False,
                  'Defence Against Dark Magic': False,
                  'History of Magic': False,
                  'Potions': False,
                  'Transfiguration': False}

def test_staticmethod_passed_with_passed_grades():
    assert Pupil.passed('E') == True
    assert Pupil.passed('Excellent') == True
    assert Pupil.passed('G') == True
    assert Pupil.passed('Good') == True
    assert Pupil.passed('A') == True
    assert Pupil.passed('Acceptable') == True

def test_staticmethod_passed_with_not_passed_grades():
    assert Pupil.passed('P') == False
    assert Pupil.passed('Poor') == False
    assert Pupil.passed('H') == False
    assert Pupil.passed('Horrible') == False

def test_staticmethod_passed_default_return_value():
    assert Pupil.passed('D') == False

def test_repr_output(capfd, luke):
    print(luke)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Pupil(name='Luke Bery', birthyear=2008, sex='male', start_year=2020)"

def test_learn_spell_hex_if_not_being_evil(capfd, luke, rectaro):
    luke.learn_spell(rectaro)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'How dare you study a hex or curse?!'

def test_learn_spell_charm_if_being_too_young(capfd, luke, liberula):
    luke.learn_spell(liberula)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Luke Bery is too young to study this spell!"

def test_learn_spell_charm_if_being_too_young_but_highly_intelligent(capfd, lissy, liberula):
    lissy.learn_spell(liberula)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Lissy Spinster now knows 'The Liberula charm'"

def test_learn_spell(capfd, luke, stuporus_ratiato):
    luke.learn_spell(stuporus_ratiato)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Luke Bery now knows 'The Stuporus Ratiato charm'"
    assert stuporus_ratiato in luke.known_spells

def test_cast_spell_curse(capfd, luke, fiera_satanotis):
    luke.cast_spell(fiera_satanotis)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'This is dark magic - stay away from performing curses!'

def test_cast_known_spell(capfd, luke, stuporus_ratiato):
    luke.learn_spell(stuporus_ratiato)
    assert luke.cast_spell(stuporus_ratiato) == 'Luke Bery: Stuporus Ratiato!'
