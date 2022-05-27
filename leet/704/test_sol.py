import pytest
from sol import Solution


@pytest.mark.parametrize(
    "test_input, test_target, expected",
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
    ],
)
def test_sol(test_input, test_target, expected) -> None:
    s = Solution()
    assert s.solve(test_input, test_target) == expected
