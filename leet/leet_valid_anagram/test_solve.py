from algosolve import Solution

def test_solve():
    solve = Solution()
    assert solve.isAnagram("bob","obb") == True
    assert solve.isAnagram("tuple", "tuppple") == False