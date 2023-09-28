class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        res, temp = 1, nums[0]

        for i in nums[1:]:
            if abs(i - temp) > k:
                temp = i
                res += 1

        return res
