import solve

def test_TwoSum():
    solution = solve.Solution()
    assert solution.twoSum([0,1,2,3,5,10,22,25],23) == "Yes for now"
    assert solution.twoSum([5,25,75], 100) == "Yes for now"