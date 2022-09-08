class Solution:
    def maxScore(self, s: str) -> int:
        l, r, m = 0, 0, 0
        l = s[0].count("0")
        r = s[1:].count("1")
        m = max(m, l + r)
        for i in range(1, len(s) - 1):
            if s[i] == "0": l += 1
            else: r -= 1
            m = max(m, l + r)
        return m
