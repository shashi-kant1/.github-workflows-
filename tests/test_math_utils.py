
import pytest

from demo_app.math_utils import add, is_even


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


@pytest.mark.parametrize("value, expected", [
    (0, True),
    (1, False),
    (2, True),
    (99, False),
])
def test_is_even(value, expected):
    assert is_even(value) == expected
