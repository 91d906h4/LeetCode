class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        for i in range(0, size+1):
            if i not in nums:
                return i
