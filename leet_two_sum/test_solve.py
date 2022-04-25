import algosolve 

def test_two_sum():
    solve = algosolve.Solution()
    assert solve.twoSum([2,7,15,19],9) == [0,1]
    assert solve.twoSum([3,4,2,5],6) == [1,2]
    assert solve.twoSum([2,3,3,4,4,7],8) == [3,4]