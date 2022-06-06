class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in t:
            if not s: break
            if i == s[0]: s = s.replace(i, "", 1)
        return len(s) == 0
