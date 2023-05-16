

import pytest

from game.hero_managerment import HeroManagement
from test_game_by_data.load_utils import LoadUtils

class TestHero:
    def setup_class(self):
        print("这是一个测试类")

    def setup_method(self):
        print("这是一个方法级别的前置处理")

    def teardown_method(self):
        print("这是一个方法级别的后置处理")

    def teardown_class(self):
        print("这是后置处理")

    # 血量 - 有效等价类（数字）& 边界值（添加成功）
    @pytest.mark.parametrize("volume", LoadUtils.load_yaml("volume_data.yaml")["success"])
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







    # 血量 - 边界值（添加失败）
    @pytest.mark.parametrize("volume", [0, 100], ids=["边界值为0", "边界值为100"])
    def test_create_hero_fail(volume):
        hero_management = HeroManagement()
        hero_management.create_hero("jinx", volume, 20)
        res = hero_management.find_hero("jinx")
        assert res == False


    #@pytest.mark.parametrize("volume", LoadUtils.load_yaml("volume_data.yaml")["success"])
    @pytest.mark.run(order=2)
    def test_create_hero_with_valid_volume(self, get_hero):
        hero_management = HeroManagement()
        hero_management.create_hero("jinx", get_hero, 20)
        res = hero_management.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("volume") == get_hero

    # 血量 - 无效等价类（非数字（字符串，布尔型））
    @pytest.mark.parametrize("volume", LoadUtils.load_yaml("volume_data.yaml")["fail"])
    @pytest.mark.run(order=1)
    def test_create_hero_with_invalid_volume(self, volume):
        hero_management = HeroManagement()
        hero_management.create_hero("jinx", volume, 20)
        res = hero_management.find_hero("jinx")
        assert res == False


