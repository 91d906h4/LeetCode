class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum(map(int, list(''.join(map(str, nums))))))
