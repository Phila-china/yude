

import pytest

from game.hero_managerment import HeroManagement

# 姓名 - 有效等价类（字符串）
@pytest.mark.parametrize("name", ["jinx", "ez"])
def test_create_hero_with_valid_name(name):
    hero_management = HeroManagement()
    hero_management.create_hero(name, 20, 20)
    res = hero_management.find_hero(name)
    assert res.get('name') == name

# 姓名 - 无效等价类（非字符串（数字，布尔型））
@pytest.mark.parametrize("name", [1, 5.5, True])
def test_create_hero_with_invalid_name(name):
    hero_management = HeroManagement()
    hero_management.create_hero(name, 20, 20)
    res = hero_management.find_hero(name)
    assert res == False

# 血量 - 有效等价类（数字）
@pytest.mark.parametrize("volume", [20, 18])
def test_create_hero_with_valid_volume(volume):
    hero_management = HeroManagement()
    hero_management.create_hero("jinx", volume, 20)
    res = hero_management.find_hero("jinx")
    assert res.get("name") == "jinx"
    assert res.get("volume") == volume

# 血量 - 无效等价类（非数字（字符串，布尔型））
@pytest.mark.parametrize("volume", ["13", False])
def test_create_hero_with_invalid_volume(volume):
    hero_management = HeroManagement()
    hero_management.create_hero("jinx", volume, 20)
    res = hero_management.find_hero("jinx")
    assert res == False

# 血量 - 边界值（添加成功）
@pytest.mark.parametrize("volume", [1,2,98,99])
def test_create_hero_success(volume):
    hero_management = HeroManagement()
    hero_management.create_hero("jinx", volume, 20)
    res = hero_management.find_hero("jinx")
    assert res.get("name") == "jinx"
    assert res.get("volume") == volume

# 血量 - 边界值（添加失败）
@pytest.mark.parametrize("volume", [0, 100], ids=["边界值为0", "边界值为100"])
def test_create_hero_fail(volume):
    hero_management = HeroManagement()
    hero_management.create_hero("jinx", volume, 20)
    res = hero_management.find_hero("jinx")
    assert res == False

# 攻击力 - 有效等价类（正整数）
@pytest.mark.parametrize("power", [20, 100])
def test_create_hero_with_valid_power(power):
    hero_management = HeroManagement()
    hero_management.create_hero("jinx", 20, power)
    res = hero_management.find_hero("jinx")
    assert res.get("name") == "jinx"
    assert res.get("power") == power

# 攻击力 - 无效等价类（0，-1，浮点数，非数字（字符串，布尔型））
@pytest.mark.parametrize("power", [0, -1, 1.5, "33", False])
def test_create_hero_with_invalid_power(power):
    hero_management = HeroManagement()
    hero_management.create_hero("jinx", 20, power)
    res = hero_management.find_hero("jinx")
    assert res == False










