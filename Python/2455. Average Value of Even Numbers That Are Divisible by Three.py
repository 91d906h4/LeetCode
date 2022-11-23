class Solution:
    def averageValue(self, nums: List[int]) -> int:
        temp = [x for i, x in enumerate(nums) if x % 6 == 0]
        return sum(temp) // len(temp) if temp != [] else 0
