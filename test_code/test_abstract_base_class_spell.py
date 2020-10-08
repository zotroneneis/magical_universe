import pytest
from magical_universe import Spell, Charm, Transfiguration, Hex, Curse, Jinx, HealingSpell, CounterSpell

@pytest.fixture
def stuporus_ratiato():
    return Charm.stuporus_ratiato()

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

def test_instantiating_base_class_raises_exception():
    with pytest.raises(TypeError):
        spell = Spell()

def test_correctness_of_charm_attributes(stuporus_ratiato):
    assert stuporus_ratiato.name == 'The Stuporus Ratiato charm'
    assert stuporus_ratiato.incantation == 'Stuporus Ratiato'
    assert stuporus_ratiato.effect == 'Makes objects fly'
    assert stuporus_ratiato.min_year == 1
    assert stuporus_ratiato.difficulty == 'Simple'

def test_cast_charm(stuporus_ratiato):
    assert stuporus_ratiato.cast() == 'Stuporus Ratiato!'

def test_repr_output_charm(capfd, stuporus_ratiato):
    print(stuporus_ratiato)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Charm(name='The Stuporus Ratiato charm', incantation='Stuporus Ratiato', effect='Makes objects fly', difficulty='Simple', min_year=1)"

def test_charm_defining_feature(stuporus_ratiato):
    assert stuporus_ratiato.defining_feature == "Alteration of the object's inherent qualities, " \
                                                "that is, its behaviour and capabilities"


def test_correctness_of_transfiguration_attributes(alteraror_canieo):
    assert alteraror_canieo.name == 'The Alteraro Canieo transfiguration'
    assert alteraror_canieo.incantation == 'Alteraro Canieo'
    assert alteraror_canieo.effect == 'Turns an object into a can'
    assert alteraror_canieo.difficulty == 'Simple'
    assert alteraror_canieo.min_year == 2

def test_cast_transfiguration(alteraror_canieo):
    assert alteraror_canieo.cast() == 'Alteraro Canieo!'

def test_repr_output_transfiguration(capfd, alteraror_canieo):
    print(alteraror_canieo)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Transfiguration(name='The Alteraro Canieo transfiguration', incantation='Alteraro Canieo', effect='Turns an object into a can', difficulty='Simple', min_year=2)"

def test_transfiguration_defining_feature(alteraror_canieo):
    assert alteraror_canieo.defining_feature == "Alteration of the object's form or appearance"

def test_correctness_of_jinx_attributes(inceptotis):
    assert inceptotis.name == 'The Inceptotis jinx'
    assert inceptotis.incantation == 'Inceptotis'
    assert inceptotis.effect == 'Makes a person talk baby talk'
    assert inceptotis.difficulty == 'Simple'

def test_cast_jinx(inceptotis):
    assert inceptotis.cast() == 'Inceptotis!'

def test_repr_output_jinx(capfd, inceptotis):
    print(inceptotis)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Jinx(name='The Inceptotis jinx', incantation='Inceptotis', effect='Makes a person talk baby talk', difficulty='Simple', min_year=1)"

def test_jinx_defining_feature(inceptotis):
    assert inceptotis.defining_feature ==  "Minor darf magic - " \
                                         "a spell whose effects are irritating but amusing, " \
                                         "almost playful and of minor inconvenience to the target"

def test_correctness_of_hex_attributes(rectaro):
    assert rectaro.name == 'The Rectaro hex'
    assert rectaro.incantation == 'Rectaro'
    assert rectaro.effect == 'Exchanges a persons arms and legs'
    assert rectaro.difficulty == 'Difficult'

def test_cast_hex(rectaro):
    assert rectaro.cast() == 'Rectaro!'

def test_repr_output_hex(capfd, rectaro):
    print(rectaro)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Hex(name='The Rectaro hex', incantation='Rectaro', effect='Exchanges a persons arms and legs', difficulty='Difficult', min_year=5)"

def test_hex_defining_feature(rectaro):
    assert rectaro.defining_feature ==  "Medium dark magic - " \
                                        "Affects an object in a negative manner. " \
                                        "Major inconvenience to the target."

def test_correctness_of_curse_attributes(fiera_satanotis):
    assert fiera_satanotis.name == 'Torture curse'
    assert fiera_satanotis.incantation == 'Fiera Satanotis'
    assert fiera_satanotis.effect == 'Tortures a person, makes person suffer deeply'
    assert fiera_satanotis.difficulty == 'Difficult'
    assert fiera_satanotis.min_year == 6

def test_cast_curse(fiera_satanotis):
    assert fiera_satanotis.cast() == 'Fiera Satanotis!'

def test_repr_output_curse(capfd, fiera_satanotis):
    print(fiera_satanotis)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Curse(name='Torture curse', incantation='Fiera Satanotis', effect='Tortures a person, makes person suffer deeply', difficulty='Difficult', min_year=6)"

def test_curse_defining_feature(fiera_satanotis):
    assert fiera_satanotis.defining_feature == "Worst kind of dark magic - " \
                                            "Intended to affect an object in a strongly negative manner."

def test_correctness_of_counter_spell_attributes(mufindo_immolim):
    assert mufindo_immolim.name == 'The Mufindo Immolim counter spell'
    assert mufindo_immolim.incantation == 'Mufindo Immolim'
    assert mufindo_immolim.effect == 'Counteracts the immobilisation spell that prevents a person from moving'
    assert mufindo_immolim.difficulty == 'Simple'

def test_cast_counter_spell(mufindo_immolim):
    assert mufindo_immolim.cast() == 'Mufindo Immolim!'

def test_repr_output_counter_spell(capfd, mufindo_immolim):
    print(mufindo_immolim)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "CounterSpell(name='The Mufindo Immolim counter spell', incantation='Mufindo Immolim', effect='Counteracts the immobilisation spell that prevents a person from moving', difficulty='Simple', min_year=1)"

def test_counter_spell_defining_feature(mufindo_immolim):
    assert mufindo_immolim.defining_feature == "Inhibites the effects of another spell"

def test_correctness_of_healing_spell_attributes(porim_perfite):
    assert porim_perfite.name == 'Wound healing spell'
    assert porim_perfite.incantation == 'Porim Perfite'
    assert porim_perfite.effect == "Heals all kinds of wounds, even bad ones"
    assert porim_perfite.difficulty == 'Difficult'
    assert porim_perfite.min_year == 5

def test_cast_healing_spell(porim_perfite):
    assert porim_perfite.cast() == 'Porim Perfite!'

def test_repr_output_healing_spell(capfd, porim_perfite):
    print(porim_perfite)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "HealingSpell(name='Wound healing spell', incantation='Porim Perfite', effect='Heals all kinds of wounds, even bad ones', difficulty='Difficult', min_year=5)"

def test_healing_spell_defining_feature(porim_perfite):
    assert porim_perfite.defining_feature == "Improves the condition of a living object"

