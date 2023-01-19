class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        s = sum(nums)

        nums.sort(reverse = True)

        for i in range(len(nums)):
            s -= nums[i] * 2
            if s < 0: return nums[:i + 1]
