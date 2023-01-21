class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        res, l = 0, len(nums)

        for i in range(l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k] and i != k:
                        res += 1
        
        return res
