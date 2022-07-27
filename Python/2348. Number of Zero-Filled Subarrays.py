class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        if 0 not in set(nums): return 0

        def helper(num):
            if num == 1: return 1
            temp =  num ** 2 - helper(num - 1)
            return temp

        nums.append(1)
        hoge, temp = [], ""
        for i in nums:
            if i == 0: temp += "0"
            else:
                hoge.append(temp)
                temp = ""
        hoge = [x for x in hoge if x != ""]

        result = 0
        for i in hoge:
            result += helper(len(i))
        return result
