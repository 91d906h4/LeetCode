class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        result = 100001
        for i in nums:
            if abs(i) < abs(result):
                result = i
            elif abs(i) == abs(result):
                result = max(result, i)
        return result
