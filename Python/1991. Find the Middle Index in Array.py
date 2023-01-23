class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l, r = 0, sum(nums)

        for i in range(len(nums)):
            if l == r - nums[i]: return i

            l += nums[i]
            r -= nums[i]
        
        return -1
