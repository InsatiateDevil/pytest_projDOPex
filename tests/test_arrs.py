import pytest

from utils import arrs

list_coll = [1, 2, 3, 4]


@pytest.fixture
def coll():
    return list_coll.copy()


def test_get(coll):
    assert arrs.get(coll, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(coll):
    assert arrs.my_slice(coll, 1, 3) == [2, 3]
    assert arrs.my_slice(coll, 1) == [2, 3, 4]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(coll) == [1, 2, 3, 4]
