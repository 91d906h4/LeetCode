import numpy as np

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        temp = [0] * size
        temp[0] = nums[0]
        counter = nums[0]
        for i in range(1, size):
            if nums[i] + counter > nums[i]:
                counter += nums[i]
            else:
                counter = nums[i]
            temp[i] = counter
        return np.amax(temp)
