import numpy as np

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         size = len(nums)
#         temp = [0] * size
#         temp[0] = nums[0]
#         counter = nums[0]
#         for i in range(1, size):
#             if nums[i] + counter > nums[i]:
#                 counter += nums[i]
#             else:
#                 counter = nums[i]
#             temp[i] = counter
#         return np.amax(temp)

#         max_, temp = -float("inf"), -float("inf")
#         for i in nums:
#             if i + temp > i:
#                 temp += i
#             else:
#                 temp = i
#             max_ = max(max_, temp)
#         return max_

        temp = result = nums[0]
        for i in nums[1:]:
            temp = max(i, temp + i)
            result = max(temp, result)
        return result
