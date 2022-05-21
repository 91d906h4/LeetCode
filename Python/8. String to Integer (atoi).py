class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        temp = ""
        n = 0
        for i in list(s):
            if (i == "-" or i == "+") and n == 0:
                temp = temp + i
                n += 1
            elif i.isdigit():
                temp = temp + i
                n += 1
            else:
                break
        if len(temp) == 0 or temp == "-" or temp == "+": return 0
        temp = int(temp)
        if temp > pow(2, 31) - 1: return pow(2, 31) - 1
        elif temp < pow(2, 31) * -1: return pow(2, 31) * -1
        else: return temp
