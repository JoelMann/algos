import pytest
from sol import Solution


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (14, 6),
        (8,4),
        (123,12),
    ],
)
def test_sol(test_input, expected):
    s = Solution()
    assert s.solve(test_input) == expected
