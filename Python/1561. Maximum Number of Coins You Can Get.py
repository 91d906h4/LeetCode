class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        len_ = len(piles)
        result = 0
        for i in range(len_ // 3, len_, 2):
            result += piles[i]
        return result
