"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest


@pytest.mark.run(order=1)
def test_one():
    print("test1")

@pytest.mark.run(order=3)
def test_two():
    print("test2")

@pytest.mark.run(order=2)
def test_three():
    print("test3")

@pytest.mark.run(order=4)
def test_four():
    print("test4")