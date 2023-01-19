class Solution:
    def minSteps(self, s: str, t: str) -> int:
        temp, sc, tc = 0, Counter(s), Counter(t)

        for i, x in tc.items():
            if i in sc: temp += min(x, sc[i]) * 2
        
        return len(s + t) - temp
