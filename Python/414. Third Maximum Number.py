class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        temp = set(nums)
        temp = list(temp)
        temp.sort(reverse = True)
        if len(temp) < 3: return max(temp)
        else: return temp[2]
