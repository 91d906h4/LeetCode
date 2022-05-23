class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0: return "0"
        result = []
        while n != 0:
            n, i = divmod(n, -2)
            if i < 0: n, i = n + 1, i + 2
            result.append(str(i))
        return "".join(result)[::-1]
