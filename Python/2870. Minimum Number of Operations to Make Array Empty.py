class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = {}
        res = 0

        for i in nums:
            if i not in d: d[i] = 1
            else: d[i] += 1

        for v in d.values():
            if v == 1: return -1

            res += v // 3
            if v % 3: res += 1

        return res
