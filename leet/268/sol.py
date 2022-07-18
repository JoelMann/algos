"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

"""


class Solution:
    def solve(self, nums: list[int]) -> int:
        contains = set(nums)
        for val in range(len(nums)+1):
            if val not in contains:
                return val


def main():
    pass


if __name__ == "__main__":
    exit(main())
