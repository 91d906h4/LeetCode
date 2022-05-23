class Solution:
    def findGCD(self, nums: List[int]) -> int:
#         x, n = max(nums), min(nums)
#         while n != 0: x, n = n, x % n
#         return x

        return gcd(max(nums), min(nums))
