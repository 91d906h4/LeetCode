class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 1 or high % 2 == 1: n = 1
        else: n = 0
        return (high - low) // 2 + n
