class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, temp = 0, 0, {}

        while j < len(nums):
            c = nums[j]

            if c not in temp: temp[c] = 1
            else: temp[c] += 1

            if temp[c] <= 2:
                nums[i] = nums[j]
                i += 1
                j += 1
            else: j += 1

        while i < len(nums): del nums[-1]
