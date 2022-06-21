class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        result = []
        m = 0
        for i in s:
            m = max(m, len(i))
        for i in range(m):
            temp = ""
            for j in range(len(s)):
                if i >= len(s[j]): temp += " "
                else: temp += s[j][i]
            result.append(temp.rstrip())
        return result
