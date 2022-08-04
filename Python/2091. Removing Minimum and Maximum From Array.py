class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        l = len(nums)
        m, n = nums.index(max(nums)), nums.index(min(nums))
        m, n = max(m, n), min(m, n)
        a, b, c = m + 1, l - n, n + (l - m) + 1
        return min(a, b, c)
