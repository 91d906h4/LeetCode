class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        pointer = 0
        result = []
        for i in nums:
            pointer = pointer * 2 + i
            result.append(pointer % 5 == 0)
        return result
