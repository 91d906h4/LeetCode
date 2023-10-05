class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = {}

        for i in nums:
            if i not in temp: temp[i] = 0
            else: temp[i] = -1

        for i in temp:
            if temp[i] == 0: return i

        return -1
