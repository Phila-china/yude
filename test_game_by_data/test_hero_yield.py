"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest


# from pytest_practice.test_game_by_data.load_utils import LoadUtils
from game.hero_managerment import HeroManagement

# 测试类与测试类的定义


@pytest.fixture()
def data():
    print("测试之前操作的内容")
    yield 1
    print("测试之后操作的内容")

class TestHero:



    def test_create_hero_volume_success(self, data):
        """
        边界值以及等价类场景的测试用例
        """
        # print(f"英雄AD的血量为{volume}")
        hero_mangement = HeroManagement()
        hero_mangement.create_hero("jinx", data,20)
        res = hero_mangement.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("volume") == data

class TestHero2:
    # **所有的方法**执行之前进行执行。
    # **所有的方法**执行之前进行执行。

    def test_create_hero_volume_success(self, data):
        """
        边界值以及等价类场景的测试用例
        """
        # print(f"英雄AD的血量为{volume}")
        hero_mangement = HeroManagement()
        hero_mangement.create_hero("jinx", data,20)
        res = hero_mangement.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("volume") == data

class TestHero3:
    # **所有的方法**执行之前进行执行。
    # **所有的方法**执行之前进行执行。

    def test_create_hero_volume_success(self, data):
        """
        边界值以及等价类场景的测试用例
        """
        # print(f"英雄AD的血量为{volume}")
        hero_mangement = HeroManagement()
        hero_mangement.create_hero("jinx", data,20)
        res = hero_mangement.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("volume") == data
