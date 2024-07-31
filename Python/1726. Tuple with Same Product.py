class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # t: Table to store productions.
        # l: length of nums.
        # r: result.

        t, l, r = {}, len(nums), 0

        for i in range(l):
            for j in range(i + 1, l):
                s = nums[i] * nums[j]
                t[s] = t[s] + 1 if s in t else 1

        for i in t.values():
            r += i * (i - 1) * 4

        return r
