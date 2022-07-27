class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        hoge, fuga = nums[0], sum(nums[1:])
        result = 0
        for i in range(1, len(nums)):
            if hoge >= fuga: result += 1
            hoge += nums[i]
            fuga -= nums[i]
        return result
