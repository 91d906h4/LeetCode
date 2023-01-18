class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s, t = Counter(s), Counter(t)

        for i in t: s[i] = abs(t[i] - s[i])
        
        return sum(s.values()) // 2
