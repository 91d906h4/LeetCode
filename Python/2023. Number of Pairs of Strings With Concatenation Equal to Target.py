class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        result = 0
        l = len(nums)
        for i in range(l):
            for j in range(l):
                if i == j: continue
                if nums[i] + nums[j] == target: result += 1
        return result
