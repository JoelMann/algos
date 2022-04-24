from algosolve import Solution

def test_solve():
    solve = Solution()
    assert solve.containsDuplicate([1,2,3,4,5,1]) == True
    assert solve.containsDuplicate([9,8,7,65,4,43245,2345,12,45,34,2]) == False