class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m, r, t = 0, 0, Counter()
        for i in range(len(s)):
            t[s[i]] += 1
            m = max(t.values())
            if r - m < k: r += 1
            else: t[s[i - r]] -= 1
        return r
