class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        xmin = 10001
        xresult = 0
        i = 0
        while i < size:
            xresult = max(xresult, prices[i] - xmin)
            xmin = min(xmin, prices[i])
            i += 1
        return xresult
