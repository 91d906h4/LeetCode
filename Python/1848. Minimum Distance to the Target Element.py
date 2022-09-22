class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        m = len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                m = min(m, abs(start - i))
        return m
