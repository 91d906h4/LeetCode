class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        half_size = size / 2
        nums.sort()
        a = 0
        for i in range(0, half_size):
            if a < nums[i]+nums[size-1-i]:
                a = nums[i]+nums[size-1-i]
        return a
