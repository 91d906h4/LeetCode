class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        result = 100001
        nums.sort()
        temp = k - 1
        for i in range(0, len(nums) - temp):
            print(nums[i], nums[i + temp])
            result = min(result, abs(nums[i] - nums[i + temp]))
        return result
