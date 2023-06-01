class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0

        for i, v in enumerate(nums):
            if i > m: return False
            m = max(m, i + v)

        return True
