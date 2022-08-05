class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        r = []
        for i in range(len(nums)):
            t, j = nums[i + 1:], nums[i]
            if j + k in t: r.append(j * 2 + k)
            if j - k in t: r.append(j * 2 - k)
        return len(set(r))
