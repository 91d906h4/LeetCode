class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a, b, c = str(bin(a))[2:], str(bin(b))[2:], str(bin(c))[2:]
        la, lb, lc = len(a), len(b), len(c)

        m = max(la, lb, lc)

        if la < m: a = "0" * (m - la) + a
        if lb < m: b = "0" * (m - lb) + b
        if lc < m: c = "0" * (m - lc) + c

        print(a, b, c)

        res = 0

        for i in range(m):
            if c[i] == a[i] and c[i] == b[i]: continue
            elif c[i] != a[i] and c[i] != b[i]: res += 1 + (a[i] == "1")
            else: res += c[i] == "0"

        return res
