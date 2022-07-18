
class Solution:
     def myAtoi(self, s: str) -> int:
        lookup = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6": 6, "7":7, "8":8, "9":9}
        s = list(s)
        res = []
        for char in s:
            if char in lookup:
                res.append(lookup[char])
        integer = 0
        while res[0] == 0:
            res.pop()
        res.reverse()
        for index,val in enumerate(res):
            integer += val*pow(10, index)
        return integer