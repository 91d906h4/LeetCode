class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        temp = {}

        for i in nums:
            if (k - i) in temp and temp[k - i] > 0: temp[k - i] -= 1; res += 1
            elif i not in temp: temp[i] = 1
            else: temp[i] += 1

        return res
