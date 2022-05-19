class Solution:
    def thirdMax(self, nums: List[int]) -> int:
#         if len(set(nums)) < 3: return max(nums)
#         else: return sorted(set(nums), reverse = True)[2]

        temp = set(nums)
        temp = list(temp)
        temp.sort(reverse = True)
        if len(temp) < 3: return max(temp)
        else: return temp[2]
