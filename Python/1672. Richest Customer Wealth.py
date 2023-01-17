class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
#         max_ = -1
#         for i in accounts:
#             max_ = max(max_, sum(i))
#         return max_

        return max(map(sum, accounts))
