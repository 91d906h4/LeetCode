class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        if nums == []: return 0
        i, res = 0, 0
        while i + 1 < len(nums):
            if nums[i] == nums[i + 1]:
                nums.pop(i)
                res += 1
            else: i += 2
        return res + (1 if len(nums) % 2 == 1 else 0)
