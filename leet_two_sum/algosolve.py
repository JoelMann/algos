#04/24/2022 17:02	Accepted	149 ms	16 MB -> Im not happy with this
#I'll want to review a more elegant lookup
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        positions = {}
        for index, num in enumerate(nums):
            if num not in positions:
                positions[num] = [index]
            else:
                positions[num].append(index)
        for index, num in enumerate(nums):
            x = target - num
            if x in positions:
                second_index = positions[x][-1]
                if x == num and len(positions[x]) == 1:
                    continue
                return [index, second_index]