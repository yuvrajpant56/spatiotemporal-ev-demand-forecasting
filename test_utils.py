# test_utils.py
from utils import convert_to_seconds

def test_convert_to_seconds():
    assert convert_to_seconds("01:30:00") == 5400
    assert convert_to_seconds("00:00:10") == 10
    assert convert_to_seconds(None) is None
    assert convert_to_seconds("00:00:00") == 0

