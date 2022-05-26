class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, isqrt(c)
        while l <= r:
            m = l * l + r * r
            if m > c: r -= 1
            elif m < c: l += 1
            else: return True
        return False
