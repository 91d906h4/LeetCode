class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def helper(num):
            num.sort()
            t = num[1] - num[0]
            for i in range(len(num) - 1):
                if num[i + 1] - num[i] != t: return False
            return True

        result = []
        for i in range(len(l)):
            temp = nums[l[i]:r[i] + 1]
            result.append(helper(temp))
        return result
