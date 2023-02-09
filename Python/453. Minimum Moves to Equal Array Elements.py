class Solution:
    def minMoves(self, nums: List[int]) -> int:
#         m, res = min(nums), 0

#         for i in nums: res += i - m

#         return res

        return sum(nums) - min(nums) * len(nums)
