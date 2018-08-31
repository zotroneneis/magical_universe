import pytest
import datetime
from magical_universe.magical_universe import Pupil, Charm, Transfiguration, Hex, Curse, Jinx, HealingSpell, CounterSpell

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
def cleon():
    return Pupil.cleon()

@pytest.fixture
def cassidy():
    cassidy = Pupil.cassidy()
    cassidy.add_trait('highly intelligent')
    return cassidy

@pytest.fixture
def adrien():
    return Pupil.adrien()

@pytest.fixture
def cleon_with_friends():
    cleon = Pupil.cleon()
    cassidy = Pupil.cassidy()
    flynn = Pupil.flynn()
    cleon.befriend(cassidy)
    cleon.befriend(flynn)
    return cleon

def test_correctness_of_attributes_(cleon):
    assert cleon.name == "Cleon Bery"
    assert cleon.house == 'House of Courage'
    assert cleon.start_year == 2018
    assert cleon.pet_name == 'Cotton'
    assert cleon.pet_type == 'owl'

def test_current_year_property(cleon):
    assert cleon.current_year == (now - cleon.start_year + 1)

def test_owls_property(cleon):
    assert cleon.elms == {'Broomstick Flying': False,
                          'Art': False,
                          'Magical Theory': False,
                          'Foreign Magical Systems': False,
                          'Charms': False,
                          'Defence Against Dark Magic': False,
                          'Divination': False,
                          'Herbology': False,
                          'History of Magic': False,
                          'Potions': False,
                          'Transfiguration': False}

def test_friends_property(cleon_with_friends):
    assert cleon_with_friends.friends == "Cleon Bery's current friends are: ['Cassidy Ambergem', 'Flynn Gibbs']"

def test_cleon_befriend_cassidy(capfd, cleon, cassidy):
    cleon.befriend(cassidy)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'Cassidy Ambergem is now your friend!'

def test_befriend_house_of_ambition_member(capfd, cleon, adrien):
    cleon.befriend(adrien)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Are you sure you want to be friends with someone from House of Ambition?\nAdrien Fulford is now your friend!"

def test_delete_elms(capfd, cleon):
    del cleon.elms
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Caution, you are deleting this students' ELM's! You should only do that if she/he dropped out of school without passing any exam!"
    with pytest.raises(AttributeError):
        print(cleon.elms)

def test_set_elms_raises_ValueError_with_wrong_input_argument(capfd, cleon):
    with pytest.raises(ValueError):
        cleon.elms = 'Transfiguration'

def test_set_elms_with_passed_grade(capfd, cleon):
    cleon.elms = ("Transfiguration", "G")
    assert cleon.elms == {'Broomstick Flying': False,
                          'Art': False,
                          'Magical Theory': False,
                          'Foreign Magical Systems': False,
                          'Charms': False,
                          'Defence Against Dark Magic': False,
                          'Divination': False,
                          'Herbology': False,
                          'History of Magic': False,
                          'Potions': False,
                          'Transfiguration': True}

def test_set_elms_with_not_passed_grade(capfd, cleon):
    cleon.elms = ("Transfiguration", "H")
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'The exam was not passed so no ELM was awarded!'
    assert cleon.elms == {'Broomstick Flying': False,
                          'Art': False,
                          'Magical Theory': False,
                          'Foreign Magical Systems': False,
                          'Charms': False,
                          'Defence Against Dark Magic': False,
                          'Divination': False,
                          'Herbology': False,
                          'History of Magic': False,
                          'Potions': False,
                          'Transfiguration': False}

def test_staticmethod_passed_with_passed_grades():
    assert Pupil.passed('E') == True
    assert Pupil.passed('Exceptional') == True
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

def test_repr_output(capfd, cleon):
    print(cleon)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'Pupil(Cleon Bery, birthyear: 2008, house: House of Courage)'

def test_learn_spell_hex_if_not_being_in_house_of_ambition(capfd, cleon, rectaro):
    cleon.learn_spell(rectaro)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'How dare you study a hex or curse?!'

def test_learn_spell_hex_if_being_in_house_of_ambition(capfd, adrien, rectaro):
    adrien.learn_spell(rectaro)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'Adrien Fulford now knows spell Rectaro'
    assert rectaro in adrien.known_spells

def test_learn_spell_if_being_too_young(capfd, cleon, liberula):
    cleon.learn_spell(liberula)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Cleon Bery does not have a character trait with the name 'highly intelligent'\nCleon Bery is too young to study this spell!"

def test_learn_spell_hex_if_being_too_young_but_highly_intelligent(capfd, cassidy, liberula):
    cassidy.learn_spell(liberula)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Yes, Cassidy Ambergem is highly intelligent!\nCassidy Ambergem now knows spell Liberula"

def test_learn_spell(capfd, cleon, stuporus_ratiato):
    cleon.learn_spell(stuporus_ratiato)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'Cleon Bery now knows spell Stuporus Ratiato'
    assert stuporus_ratiato in cleon.known_spells

def test_cast_spell_curse(capfd, cleon, fiera_satanotis):
    cleon.cast_spell(fiera_satanotis)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'This is dark magic - stay away from performing curses!'

def test_cast_known_spell(capfd, cleon, stuporus_ratiato):
    cleon.learn_spell(stuporus_ratiato)
    assert cleon.cast_spell(stuporus_ratiato) == 'Cleon Bery: Stuporus Ratiato!'
