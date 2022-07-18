"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

# Note: This is log(n) speed but is terrible for memory usage
# and slow due to how much it generates. A better implementation would be 2 points
class Solution:
    def solve(self, nums: list[int], target: int) -> int:
        length = len(nums)
        pivot = length // 2
        debugPoint = nums[pivot]
        if length == 1 and nums[0] != target:
            return -1
        if nums[pivot] == target:
            return pivot
        if nums[pivot] > target:
            nums = nums[0:pivot]
            val = self.solve(nums, target)
            if val != -1:
                return val
        else:
            nums = nums[pivot:]
            val2 = self.solve(nums, target)
            if val2 != -1 or None:
                return val2 + pivot
        return -1


def main() -> None:

    s = Solution()
    s.solve([-1, 0, 3, 5, 9, 12], 2)


if __name__ == "__main__":
    main()
