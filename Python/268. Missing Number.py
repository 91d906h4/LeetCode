class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         size = len(nums)
#         for i in range(0, size+1):
#             if i not in nums:
#                 return i

#         nums_size = len(nums)
#         nums_sum = sum(nums)
#         real_sum = (1 + nums_size) * nums_size / 2
#         return real_sum - nums_sum

        return "".join(map(str, list(set(range(len(nums) + 1)) - set(nums))))
