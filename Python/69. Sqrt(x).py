class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        high, low = x // 2, 0
        while high >= low:
            mid = (high + low) // 2
            temp = mid * mid
            if temp == x:
                return mid
            elif temp > x:
                high = mid - 1
            else:
                low = mid + 1
        return high
