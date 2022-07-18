"""
278. First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""



class Solution:
    
    def __init__(self, badValue: int, listSize: int) -> None:
        
    
    def isBadVersion(self, index: int) -> bool:
    

    def solve(self, n: int) -> int:
        left, right = 0, n-1

        lastIndex, lastBool = None, None

        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(version = mid):
                right = mid
                if lastBool == False and (mid - last)


def main():
    pass


if __name__ == "__main__":
    exit(main())


"""
check middle:
if bad, somewhere before is good -> Remove everything to the right
if good, somewhere after is bad -> remove everything to the left
if bad, and last check good, and last check n == n-1, return n as first bad
"""