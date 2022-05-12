class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
#         result = []
#         temp = {}
#         len_ = len(nums)
#         for i in range(len_):
#             if nums[i] not in temp:
#                 temp[nums[i]] = 1
#             else:
#                 result.append(nums[i])
#                 break

#         for i in range(1, len_ + 1):
#             if i not in nums:
#                 result.append(i)
#                 break
#         return result

        temp = {}
        for i in range(0, len(nums)):
            if nums[i] not in temp:
                temp[nums[i]] = 1
            else:
                temp[nums[i]] += 1
        
        for i in range(1, len(nums) + 1):
            if i not in temp:
                miss = i
            elif temp[i] > 1:
                err = i
        return [err, miss]
