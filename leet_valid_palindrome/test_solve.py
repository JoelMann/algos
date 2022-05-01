import algosolve

def test_isPalindrome():
    solve = algosolve.Solution()
    assert solve.isPalindrome("olllllo") == True
    assert solve.isPalindrome("Hello World") == False