class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t, res = prices[0], 0

        for i in prices:
            if i > t: res += i - t
            t = i
        
        return res
