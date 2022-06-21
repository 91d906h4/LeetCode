class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def helper(n):
            temp = 0
            while n != 1:
                if n & 1: n = 3 * n + 1
                else: n //= 2
                temp += 1
            return temp
        hoge = {}
        for i in range(lo, hi + 1):
            hoge[i] = helper(i)
        hoge = sorted(hoge.items(), key = lambda x: x[1])
        return hoge[k - 1][0]
