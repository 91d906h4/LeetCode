class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        temp, t, c, res = [], s[0], 0, 0

        s += " "

        for i in s:
            if i == t: c += 1
            else:
                temp.append(c)
                c = 1
                t = i

        for i in range(len(temp) - 1): res += min(temp[i], temp[i + 1])

        return res
