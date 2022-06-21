class Solution:
    def makeGood(self, s: str) -> str:
        temp = True
        while temp:
            temp = False
            for i in range(len(s) - 1):
                if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                    s = s.replace(s[i] + s[i + 1], "", 1)
                    temp = True
                    break
        return s
