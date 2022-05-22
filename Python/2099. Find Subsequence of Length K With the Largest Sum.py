class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        max_ = nums[:k]
        for i in range(k, len(nums)):
            if min(max_) < nums[i]:
                max_.remove(min(max_))
                max_.append(nums[i])
        return max_
