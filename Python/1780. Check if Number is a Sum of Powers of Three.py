class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(15, -1, -1):
            temp = pow(3, i)
            if n - temp >= 0: n -= temp
        return n == 0
