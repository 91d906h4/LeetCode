class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [-1, -1] if target not in nums else [nums.index(target), len(nums) - nums[::-1].index(target) - 1]
