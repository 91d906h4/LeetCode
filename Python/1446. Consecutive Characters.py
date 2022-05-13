class Solution:
    def maxPower(self, s: str) -> int:
        temp, result = 1, 0
        if len(s) == 1: return 1
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                temp += 1
            else:
                temp = 1
            result = max(result, temp)
        return result
