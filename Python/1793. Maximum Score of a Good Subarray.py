class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res = t = nums[k]
        i, j, n, m = k, k, len(nums), 2

        while i > 0 or j < n - 1:
            if (nums[i - 1] if i > 0 else 0) < (nums[j + 1] if j < n - 1 else 0): j += 1
            else: i -= 1

            t = min(t, nums[i], nums[j])
            res = max(res, t * m)
            m += 1

        return res
