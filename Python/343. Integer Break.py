class Solution:
    def integerBreak(self, n: int) -> int:
#         if n < 4: return n - 1
#         result = 1
#         while n > 4:
#             result *= 3
#             n -= 3
#         return result * n

        return n - 1 if n < 4 else pow(3, (n - 2) // 3) * ((n - 2) % 3 + 2)
