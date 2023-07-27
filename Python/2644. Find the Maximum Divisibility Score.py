class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res = {}

        for i in divisors:
            temp = 0

            for j in nums:
                if j % i == 0: temp += 1

            res[i] = temp

        m = max(res.values())
        r = float("inf")

        for i, x in res.items():
            if x == m and i < r: r = i

        return r
