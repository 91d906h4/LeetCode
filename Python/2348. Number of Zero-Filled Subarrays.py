class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        if 0 not in set(nums): return 0

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
            result += (len(i) * (len(i) + 1)) // 2
        return result
