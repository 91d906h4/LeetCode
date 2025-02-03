class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        result = 0
        order = 0
        temp = 1

        for i in range(1, len(nums)):
            if order != -1 and nums[i-1] < nums[i]:
                order =  1
                temp += 1
            elif order != 1 and nums[i-1] > nums[i]:
                order = -1
                temp += 1
            else:
                order *= -1
                result = max(result, temp)
                temp = 1 + int(nums[i-1] != nums[i])

        result = max(result, temp)

        return result
