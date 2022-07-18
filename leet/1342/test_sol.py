import pytest
import sol


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (14, 6),
        (8,4),
        (123,12),
    ],
)
def test_sol(test_input, expected):
    s = sol.Solution()
    assert s.solve(test_input) == expected
