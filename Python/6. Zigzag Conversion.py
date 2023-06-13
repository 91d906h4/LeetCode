class Solution:
    def convert(self, s: str, numRows: int) -> str:
        temp = []

        if numRows == 1: return s

        for i in range(numRows):
            t = [0] * len(s)
            temp.append(t)

        i, j = 0, -1
        d = 0

        for x in s:
            if d == 0:
                if j + 1 == numRows:
                    d = 1
                    i += 1
                    j -= 1
                else: j += 1
            else:
                if j - 1 == -1:
                    d = 0
                    j += 1
                else:
                    i += 1
                    j -= 1

            temp[j][i] = x

        res = ""

        for i in temp:
            for j in i:
                if j != 0: res += j

        return res
