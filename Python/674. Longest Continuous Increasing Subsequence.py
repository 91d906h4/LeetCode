class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        temp, max_ = 0, 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                temp += 1
            else: temp = 0
            max_ = max(max_, temp)
        return max_ + 1
