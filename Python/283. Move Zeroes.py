class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
#         size = len(nums)
#         i, j = 0, 0
#         while j < size:
#             if(nums[i] == 0):
#                 nums.pop(i)
#                 nums.append(0)
#                 i -= 1
#             i += 1
#             j += 1

#         i, j = 0, 0
#         for j in range(len(nums)):
#             if nums[i] == 0:
#                 nums.pop(i)
#                 nums.append(0)
#             else:
#                 i += 1
#             j += 1

        nums[:] = list(filter((0).__ne__, nums)) + [0] * nums.count(0)
