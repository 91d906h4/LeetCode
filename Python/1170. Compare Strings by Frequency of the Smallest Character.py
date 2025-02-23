class Solution:
    @staticmethod
    def f(s: str) -> int:
        x = '{'
        t = defaultdict(int)

        for c in s:
            x = min(x, c)
            t[c] += 1

        return t[x]

    @staticmethod
    def bs(q: int, t: list) -> int:
        l, r = 0, len(t)

        while l < r:
            m = (l + r) // 2

            if t[m] > q: r = m
            else: l = m + 1

        return len(t) - l

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        queries = [self.f(q) for q in queries]
        words = [self.f(w) for w in words]
        res = []
        
        words.sort()

        for q in queries:
            res.append(self.bs(q, words))

        return res
