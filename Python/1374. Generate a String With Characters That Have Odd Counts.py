class Solution:
    def generateTheString(self, n: int) -> str:
        return "a" * n if n & 1 else "b" + "a" * (n - 1)
