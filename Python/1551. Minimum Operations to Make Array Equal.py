class Solution:
    def minOperations(self, n: int) -> int:
        return ceil(n / 2) * floor(n / 2)
