class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        hoge = []
        while len(nums) > 1:
            hoge = []
            for i in range(len(nums) // 2):
                if i & 1: hoge.append(max(nums[2 * i], nums[2 * i + 1]))
                else: hoge.append(min(nums[2 * i], nums[2 * i + 1]))
            nums = hoge
        return min(nums)
