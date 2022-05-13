class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result, temp = [], []
        for i in nums:
            if i in temp: continue
            if i not in result: result.append(i)
            else:
                result.remove(i)
                temp.append(i)
        for i in temp:
            if i in result: result.remove(i)
        return sum(result)
