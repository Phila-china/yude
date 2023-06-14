"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest

# 夹具套夹具。 夹具开关： 应用场景
# 已有1000条用例数据。 模块A使用。但是你不能动。
# 如果想要复用夹具的逻辑， 就可以使用套用夹具
# 如果有的场景要求数据是+1，有的场景不要求数据+1。-》 夹具开关。
@pytest.fixture
def first_entry():
    return "a"

@pytest.fixture
def order(first_entry):
    return []

# # 自动生效： 有点类似于开关。
# # 如果需要数据变化，则把开关打开。
# # 如果不需要，则把开关关闭。
@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)

# autouse 是一个开关。 等同于，在每个使用了夹具数据的测试用例里面，提前帮她们完成了数据的变化

# def setup_function():
#     order.append(first_entry)

def test_string_only(order, first_entry):
    # [] == ["a"]
    print(order)
    print(first_entry)
    assert order == [first_entry]

def test_string_and_int(order, first_entry):
    order.append(2)
    print(order)
    print(first_entry)
    assert order == [first_entry, 2]



