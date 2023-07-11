class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n, res = len(nums), 0

        for i in range(n):
            s, t = set(), -1

            for j in range(i, n):
                if nums[j] in s: t += 0
                elif nums[j] + 1 not in s and nums[j] - 1 not in s: t += 1
                elif nums[j] + 1 in s and nums[j] - 1 in s: t -= 1

                s.add(nums[j])
                res += t

        return res
