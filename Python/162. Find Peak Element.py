class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)

        if l == 1: return 0
        if l == 2: return 0 if nums[0] > nums[1] else 1
        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return l - 1

        for i in range(1, l - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]: return i
