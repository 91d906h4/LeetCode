class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = permutations(nums)
        result = []
        for i in nums:
            result.append(list(i))
        return result
