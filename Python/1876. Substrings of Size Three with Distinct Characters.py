class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        t, res = [0] + list(s[:2]), 0

        for i in s[2:]:
            t = t[1:] + [i]
            if len(set(t)) == 3: res += 1
        
        return res
