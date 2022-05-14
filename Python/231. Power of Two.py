class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 : return True
        if n % 2 != 0 or n <= 0: return False
        while n > 2:
            if n % 2 == 1:return False
            n /= 2
        return True
