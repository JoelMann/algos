"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def solve(self, nums: list[int], target: int) -> int:
        if len(nums) == 1 and nums[0] != target:
            return -1
        if nums[len(nums)//2] == target:
            return len(nums)//2
        if nums[len(nums)//2] > target:
            nums = nums[len(nums)//2:]
            return self.solve(nums, target)
        else:
            nums = nums[0:len(nums)//2]
            return self.solve(nums, target)




def main() -> None:

    s = Solution()
    s.solve([-1, 0, 3, 5, 9, 12], 9)


if __name__ == "__main__":
    main()
