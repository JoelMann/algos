import sol
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), (" ", 1), ("au", 2), ("bwf", 3)],
)
def test_sol(test_input, expected):
    so = sol.Solution()
    assert so.lengthOfLongestSubstring(test_input) == expected
