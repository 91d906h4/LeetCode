class Solution:
    def checkString(self, s: str) -> bool:
        b = 0
        for i in list(s):
            if i == 'a':
                if b == 1: return False
            else: b = 1
        return True
