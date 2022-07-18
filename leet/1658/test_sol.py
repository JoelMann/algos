import pytest
from sol import Solution


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (None, None),
    ],
)
def test_sol(test_input, expected):
    s = Solution()
    assert s.solve(test_input) == expected
