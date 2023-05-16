import allure
import pytest

from game.hero_managerment import HeroManagement


class TestHero:

    # 血量 - 有效等价类（正整数）
    @pytest.mark.valid
    @allure.step
    @pytest.mark.run(order=1)
    def test_create_hero_with_valid_volume(self, valid_equivalence_class):
        hero_management = HeroManagement()
        hero_management.create_hero("jinx", valid_equivalence_class, 20)
        res = hero_management.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("volume") == valid_equivalence_class

    # 血量 - 边界值（添加成功）
    @allure.step
    @pytest.mark.run(order=4)
    def test_create_hero_with_success_boundary_value(self, success_boundary_value):
        hero_management = HeroManagement()
        hero_management.create_hero("jinx", success_boundary_value, 20)
        res = hero_management.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("volume") == success_boundary_value

    # 血量 - 无效等价类（字符串，布尔型，浮点数）
    @allure.step
    @pytest.mark.invalid
    @pytest.mark.run(order=2)
    def test_create_hero_with_invalid_volume(self, invalid_equivalence_class):
        hero_management = HeroManagement()
        hero_management.create_hero("jinx", invalid_equivalence_class, 20)
        res = hero_management.find_hero("jinx")
        assert res == False

    # 血量 - 边界值（添加失败）
    @allure.step
    @pytest.mark.run(order=3)
    def test_create_hero_with_fail_boundary_value(self, fail_boundary_value):
        hero_management = HeroManagement()
        hero_management.create_hero("jinx", fail_boundary_value, 20)
        res = hero_management.find_hero("jinx")
        assert res == False




