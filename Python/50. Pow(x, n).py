class Solution:
    def myPow(self, x: float, n: int) -> float:
#         return pow(x, n)
#         return x ** n

        if n < 0:
            x = 1 / x
            n = abs(n)
        result = 1
        while n > 0:
            if n & 1:
                result = result * x
            x = x * x
            n >>= 1
        return result
