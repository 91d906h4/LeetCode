class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if nums.count(0) > 0: return 0
        if len([x for x in nums if x < 0]) % 2 == 0: return 1
        else: return -1
