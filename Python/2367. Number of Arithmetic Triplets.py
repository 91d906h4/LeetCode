class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        t, nums = 0, set(nums)
        for i in nums:
            if i + diff in nums and i + diff * 2 in nums: t += 1
        return t
