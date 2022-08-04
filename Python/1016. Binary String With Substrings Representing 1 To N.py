class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(n, 1, -1):
            if str(bin(i))[2:] not in s: return False
        return True
