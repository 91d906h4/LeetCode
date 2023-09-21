class Solution:
    def romanToInt(self, s: str) -> int:
        m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res, temp = 0, 0

        for i in reversed(s):
            i = m[i]
            if i >= temp: res += i; temp = i
            else: res -= i

        return res
