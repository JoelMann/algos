import sol
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [("42", 42), ("   -42", -42), ("4193 with words", 4193), (" 0042", 42), ("+42",42), ("2147483648", 2147483647),(("-2147483648", -2147483647))],
)
def test_sol(test_input, expected):
    so = sol.Solution()
    assert so.myAtoi(test_input) == expected
