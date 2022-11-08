class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)

#         Bobble Sort
#         l = len(nums)
#         for i in range(l):
#             for j in range(l - i - 1):
#                 if nums[j] > nums[j + 1]:
#                     nums[j], nums[j + 1] = nums[j + 1], nums[j]
#         return nums

#         Selection Sort
#         l = len(nums)
#         for i in range(l):
#             for j in range(i + 1, l):
#                 if nums[j] < nums[i]:
#                     nums[i], nums[j] = nums[j], nums[i]
#         return nums
