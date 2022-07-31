class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = str(bin(n)).replace("0b", "")
        for i in range(len(n) - 1):
            if n[i] == n[i + 1]: return False
        return True
