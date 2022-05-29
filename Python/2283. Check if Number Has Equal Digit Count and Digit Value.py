class Solution:
    def digitCount(self, num: str) -> bool:
        for i, j in enumerate(num):
            if num.count(str(i)) != int(j): return False
        return True
