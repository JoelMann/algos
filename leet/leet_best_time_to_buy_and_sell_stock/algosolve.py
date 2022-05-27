class Solution():
    def maxProfit(self, prices: list[int]) -> int:
        profit = [[]]

        for i,v in enumerate(prices):
                
            profit[i].append(v)
            for x in profit:
                profit[x].append(profit[i][0] - v)

        print(profit)


s= Solution()
s.maxProfit([7,1,5,3,6,4])