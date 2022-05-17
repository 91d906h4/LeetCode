class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        high, low = 2**16, 1
        mid = (high + low) // 2
        while high >= low:
            mid = (high + low) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                high = mid - 1
            elif mid * mid < num:
                low = mid + 1
            print(mid)
        return False
