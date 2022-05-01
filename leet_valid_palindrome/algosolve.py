class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        for index in range(0,int(len(s)/2)):
            if s[index] != s[(-index)-1]:
                return False
        return True