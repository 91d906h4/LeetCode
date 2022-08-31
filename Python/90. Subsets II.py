class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l, r = len(nums), []
        for i in range(1 << l):
            t = sorted([nums[j] for j in range(l) if (i & (1 << j))])
            if t not in r: r.append(t)
        return r
