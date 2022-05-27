class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup = {}

        for x in s:
            if x in lookup:
                lookup[x] += 1
            else:
                lookup[x] = 1
        
        for y in t:
            if y in lookup and lookup[y] != 0:
                lookup[y] -= 1
            else:
                return False
        if len(s) != len(t):
            return False
        return True