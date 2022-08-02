class Solution:
    def longestPalindrome(self, s: str) -> int:
        r, t = 0, 0
        for i in Counter(s).values():
            if i % 2 == 1: t = 1
            r += (i // 2) * 2
        return r + t
