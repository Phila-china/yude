import pytest
import yaml

from test_game_by_data.load_utils import LoadUtils


def test_yaml():
    data = yaml.safe_load(open("../hp_data.yaml"))
    print(data)

@pytest.mark.parametrize("data", LoadUtils.load_yaml("../hp_data.yaml"))
def test_load_data(data):
    assert data == 1