class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if n == 1: return 1
        if trust == []: return -1

        t = defaultdict(list)

        for i, j in trust: t[i].append(j)

        hoge = []

        for i in range(1, n + 1):
            if i not in t: hoge.append(i)

        if len(hoge) != 1: return -1
        hoge = hoge[0]

        for i in t.values():
            if hoge not in i: return -1

        return hoge
