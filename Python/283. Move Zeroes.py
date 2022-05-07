class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        i, j = 0, 0
        while j < size:
            print(i)
            if(nums[i] == 0):
                nums.pop(i)
                nums.append(0)
                i -= 1
            i += 1
            j += 1
