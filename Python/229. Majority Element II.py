class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums) // 3
        temp = {}

        for i in nums:
            if i not in temp: temp[i] = 1
            else: temp[i] += 1

        return [x[0] for x in temp.items() if x[1] > l]
