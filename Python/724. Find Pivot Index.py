class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums.append(0)
        hoge, fuga = 0, sum(nums[1:])
        for i in range(len(nums) - 1):
            print(hoge, fuga)
            if hoge == fuga: return i
            hoge += nums[i]
            fuga -= nums[i + 1]
        return -1
