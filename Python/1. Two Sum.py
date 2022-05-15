class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             temp = target - nums[i]
#             if temp in nums and i != nums.index(temp):
#                 return [i, nums.index(temp)]

        dict_ = {}
        for i, j in enumerate(nums):
            temp = target - j
            if temp in dict_:
                return [dict_[temp], i]
            else: dict_[j] = i
