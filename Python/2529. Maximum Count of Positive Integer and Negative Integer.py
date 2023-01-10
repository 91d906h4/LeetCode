class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l, z, temp = len(nums), 0, 0

        for i in range(l):
            n = nums[i]

            if n < 0: temp += 1
            elif n == 0: z += 1
            else: break
        
        return max(temp, l - z - temp)
