class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i, j in enumerate(prices):
            temp = 0
            for x in range(i + 1, len(prices)):
                if prices[x] <= j:
                    temp = prices[x]
                    break
            result.append(prices[i] - temp)
        return result
