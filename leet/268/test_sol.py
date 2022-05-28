import pytest
from sol import Solution


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([3,0,1], 2),
        ([0,1], 2),
        ([9,6,4,2,3,5,7,0,1], 8),
    ],
)
def test_sol(test_input, expected):
    s = Solution()
    assert s.solve(test_input) == expected
