class Solution:
    def modifyString(self, s: str) -> str:
        for i in range(len(s)):
            if s[i] == "?":
                for temp in "abcdefghijklmnopqrstuvwxyz":
                    if (i - 1 < 0 or s[i - 1] != temp) and (i + 1 >= len(s) or s[i + 1] != temp):
                        s = s.replace("?", temp, 1)
                        break
        return s
