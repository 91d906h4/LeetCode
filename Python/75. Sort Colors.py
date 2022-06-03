class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
#         hoge, fuga = [], 0
#         for i in nums:
#             if i == 0:
#                 hoge.insert(0, i)
#                 fuga += 1
#             elif i == 2:
#                 hoge.append(i)
#             else:
#                 hoge.insert(fuga, i)
#         for i in range(len(nums)):
#             nums[i] = hoge[i]

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
