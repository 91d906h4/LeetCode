class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        size = len(s1)
        for i in range(size):
            for j in range(i, size):
                temp = list(s1)
                temp[i], temp[j] = temp[j], temp[i]
                if "".join(temp) == s2: return True
        return False
