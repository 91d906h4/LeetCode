class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res, temp = [], {}

        for i in nums:
            if i in temp: res.append(i)
            else: temp[i] = 1
        
        return res
