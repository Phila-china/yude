
# pytest 用来管理公共方法、公共配置的文件
# 1. 公共的fixture。
# 2. hook函数的定制。

# 通过 scope 参数灵活控制夹具的使用具体是类级别或者其他级别。

import pytest

from test_game_by_data.load_utils import LoadUtils


# 先定义一个夹具，需要使用 (params) 参数，
# params = 参数化的数据
@pytest.fixture(params=LoadUtils.load_yaml("volume_data.yaml")["validEquivalenceClass"])
# 夹具(request) 固定格式
def valid_equivalence_class(request):
    # 需要返回 request.param 固定格式
    yield request.param
    print("有效等价类数据导入完成")

@pytest.fixture(params=LoadUtils.load_yaml("volume_data.yaml")["invalidEquivalenceClass"])
def invalid_equivalence_class(request):
    yield request.param
    print("无效等价类数据导入完成")

@pytest.fixture(params=LoadUtils.load_yaml("volume_data.yaml")["successBoundaryValue"])
def success_boundary_value(request):
    request.param = request.param+1
    yield request.param
    print("有效边界值数据导入完成")

@pytest.fixture(params=LoadUtils.load_yaml("volume_data.yaml")["failBoundaryValue"])
def fail_boundary_value(request):
    yield request.param
    print("无效边界值数据导入完成")


