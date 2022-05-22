class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp = sum(nums[:k])
        max_ = temp
        for i in range(len(nums) - k):
            temp -= nums[i]
            temp += nums[i + k]
            if temp > max_: max_ = temp
        return max_ / k
