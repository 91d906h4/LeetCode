class Solution:
    def fac(self, n: int) -> int:
        r = 1

        for i in range(1, n + 1): r *= i

        return r

    def numPrimeArrangements(self, n: int) -> int:
        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        t = 0

        for i in p:
            if i > n: break
            t += 1

        return (self.fac(t) * self.fac(n - t)) % (10 ** 9 + 7)
