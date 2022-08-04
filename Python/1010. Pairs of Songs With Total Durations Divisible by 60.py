class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        t = Counter([x % 60 for x in time])
        r = 0
        for i, j in t.items():
            if i in [0, 30]: r += j * (j - 1)
            elif 60 - i in t: r += j * t[60 - i]
        return r // 2
