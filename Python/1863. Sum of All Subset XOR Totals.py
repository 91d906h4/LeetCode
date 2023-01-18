class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        l, res = len(nums) + 1, 0

        for i in range(l):
            for j in combinations(nums, i):
                if j != (): res += reduce(lambda a, b: a ^ b, j)
        
        return res
