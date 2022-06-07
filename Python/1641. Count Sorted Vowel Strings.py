class Solution:
    def countVowelStrings(self, n: int) -> int:
#         hoge = [1] * 5
#         for _ in range(n - 1):
#             hoge = accumulate(hoge)
#         return sum(hoge)

#         dp = [1, 1, 1, 1, 1]
#         for i in range(1, n):
#             dp[1] += dp[0]
#             dp[2] += dp[1]
#             dp[3] += dp[2]
#             dp[4] += dp[3]
#         return sum(dp)

#         return (n + 1) * (n + 2) * (n + 3) * (n + 4) // 24

        return comb(n + 4, n)
