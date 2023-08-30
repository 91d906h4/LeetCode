class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j, res = 0, len(nums) - 1, 0

        while i < j:
            if nums[i] + nums[j] < target:
                res += j - i
                i += 1
            else: j -= 1

        return res
