class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result, i = 0, 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]: nums.pop(i + 1)
            else: i += 1
        for i in range(1, len(nums) - 1, 1):
            if nums[i - 1] < nums[i] > nums[i + 1] or nums[i - 1] > nums[i] < nums[i + 1]: result += 1
        return result
