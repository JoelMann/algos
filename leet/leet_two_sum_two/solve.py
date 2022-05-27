from collections import namedtuple


class Solution():
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start = 0
        end = -1
        sideSlider = "right"
        solved = False
        Left = namedtuple("Left", "val index")
        Right = namedtuple("Right", "val index")

        leftPrev = Left(99999999999,1000000000000)
        rightPrev =  Right(99999999999,1000000000000)

        for _ in range(1, 10000):

            left = Left(numbers[start], start)
            right = Right(numbers[end], end)

            if left.val + right.val == target or leftPrev.val + right.val == target or left.val + rightPrev.val == target:
                solved = True
                return "Yes for now"
            if left.val >= right.val:
                start = 0
                end = -1
                sideSlider = "left"
                continue

            if left.val + right.val > target:
                if sideSlider == 'left':
                    start += 1
                    sideSlider = 'right'
                else:
                    end -= 1
                    sideSlider = 'left'

            leftPrev = left
            rightPrev = right


summer = Solution()

print(summer.twoSum([0, 1, 2, 3, 5, 10, 22, 25], 23))
