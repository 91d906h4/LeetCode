class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        temp = 1
        while temp in nums:
            temp += 1
        return temp
