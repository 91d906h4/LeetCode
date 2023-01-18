class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, l = [[]], len(nums)

        for i in range(1, l + 1):
            for j in combinations(nums, i):
                if j not in res: res.append(j)
        
        return res
