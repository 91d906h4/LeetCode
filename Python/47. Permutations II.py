class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = permutations(nums)
        result = []
        for i in nums:
            if i not in result: result.append(i)
        return result
