class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        sort_ = sorted(s1)
        for i in range(len(s2) - size + 1):
            if sorted(s2[i:i + size]) == sort_: return True
        return False
