import pytest

from game.hero_managerment import HeroManagement

hero_management = HeroManagement()

def setup():
    hero_management.create_hero("jinx", 20, 20)

def test_update_hero():
    hero_management.update_hero("jinx", 22)
    res = hero_management.find_hero("jinx")
    assert res.get("volume") == 22


def test_delete_hero():
    hero_management.delete_hero("jinx")
    res = hero_management.find_hero("jinx")
    assert res == False

# @pytest.mark.parametrize("volume", [200, 100])
def test_create_hero():
    res = hero_management.find_hero("jinx")
    assert res != False
    assert res.get("name") == "jinx"
    assert res.get("volume") == 20
    assert res.get("power") == 20


def test_find_hero():
    res = hero_management.find_hero("jinx")
    res2 = hero_management.find_hero("ez")
    assert res.get("name") == "jinx"
    assert res2 == False
