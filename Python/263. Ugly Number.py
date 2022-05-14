class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        temp = 2
        while n >= temp and temp <= 5:
            if n % temp != 0:
                 temp += 1
            else:
                n /= temp
        return n == 1
