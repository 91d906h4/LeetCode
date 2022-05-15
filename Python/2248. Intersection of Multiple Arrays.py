class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
#         result = sorted(nums[0])
#         for i in nums:
#             j = 0
#             while j < len(result):
#                 k = result[j]
#                 if k not in i:
#                     result.remove(k)
#                     j -= 1
#                 j += 1
#         return sorted(result)

        result = set(nums[0])
        result = result.intersection(*nums)
        return sorted(result)
