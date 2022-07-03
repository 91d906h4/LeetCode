class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        t = m = len([x for x in s[:k] if x in "aeiou"])
        for i in range(k, len(s)):
            if s[i - k] in "aeiou": m -= 1
            if s[i] in "aeiou": m += 1
            t = max(t, m)
        return t
