class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        hoge, fuga = [], []
        for i in range(len(nums)):
            if i & 1: fuga.append(nums[i])
            else: hoge.append(nums[i])
        hoge.sort()
        fuga.sort(reverse = True)
        result = []
        for i in range(len(nums)):
            if i & 1: result.append(fuga.pop(0))
            else: result.append(hoge.pop(0))
        return result
