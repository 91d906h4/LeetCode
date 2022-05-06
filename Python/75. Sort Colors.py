class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        output = [0] * size
        count = [0] * 3
        for i in range(0, size):
            count[nums[i]] += 1
        for i in range(1, 3):
            count[i] += count[i-1]
        i = size-1
        while i >= 0:
            output[count[nums[i]]-1] = nums[i]
            count[nums[i]] -= 1
            i -= 1
        for i in range(0, size):
            nums[i] = output[i]
        return nums
