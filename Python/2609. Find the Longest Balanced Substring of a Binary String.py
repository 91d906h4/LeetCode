class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = []
        t, k = s[0], 0
        s += " "

        trig = False if t == "1" else True

        for i in s:
            if i == t: k += 1
            else:
                res.append(k)
                k = 1
                t = i

        m = 0

        for i in range(len(res) - 1):
            if trig: m = max(m, min(res[i], res[i + 1]))
            trig = not trig

        return m * 2
