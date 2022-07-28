class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        result = k * (k + 1) // 2
        for i in sorted(set(nums)):
            if i <= k:
                k += 1
                result += k - i
        return result
