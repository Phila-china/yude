
"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'

Test runner
Test case
Test fixtures
Test suites
Test execution：   setup/teardown
Test result formatter： collecting ... collected 2 items
Assertions：
"""
import pytest


# 在pytest 中， setup 是一个关键字
# 在 **每条** 用例执行之前执行。(6.xx)
# 在 模块的所有用例执行之前执行。(7.xx)
def setup():
    print("setup执行啦")

# 在 **每条** 用例执行之后执行。
def teardown_function():
    print("teardown执行啦")

# 如果没有使用 pytest 方式运行，那么就会当成正常的函数执行。
@pytest.mark.P0
def test_demo():
    print("12312")
    # 断言： Assertions
    assert 1==1

# Test result formatter
# collecting ... collected 2 items
#
# test_demo.py::test_demo FAILED                                           [ 50%]12312
@pytest.mark.P0
def test_assert():
    # assert True
    # assert False
    assert {"name": "111"}
    assert [1,2,3]
    assert []

def demo():
    return True


@pytest.mark.P1
# Test case， Test runner
def test_demo2():
    print("12312")
    # 断言： Assertions
    assert 1==1 # 布尔值
    # 如果断言失败了，，后面的代码就不会执行了
    assert 1 in ["1" , 1 ] # 布尔值
    assert demo() # 布尔值
    # assert 1==2
