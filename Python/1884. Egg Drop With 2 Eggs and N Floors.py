class Solution:
    def twoEggDrop(self, n: int) -> int:
        for i in range(1, n + 1):
            n -= i
            if n <= 0: return i
        return 0
