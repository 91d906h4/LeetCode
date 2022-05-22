class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        temp = list(nums)
        temp.sort(reverse = True)
        if len(temp) == 1: return 0
        if temp[0] >= temp[1] * 2: return nums.index(temp[0])
        else: return -1
