class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b: a, b = b, a % b
        return a

    def simplifiedFractions(self, n: int) -> List[str]:
        res = []

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if gcd(i, j) == 1: res.append(str(i) + "/" + str(j))

        return res
