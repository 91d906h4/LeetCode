class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_, temp = float("inf"), 0
        for i in nums:
            min_ = min(min_, temp := temp + i)
        return abs(min_) + 1 if min_ < 1 else 1
