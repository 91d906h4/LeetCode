class Solution:
    def n2s(self, n: str) -> str:
        x, counter, res = n[0], 0, []

        for i in n + "x":
            if i == x: counter += 1
            else:
                res.append([x, counter])
                x, counter = i, 1

        return res

    def s2n(self, s: list) -> int:
        res = ""

        for i in s: res += str(i[0]) + str(i[1])

        return res

    def countAndSay(self, n: int) -> str:
        res = "1"

        for i in range(1, n):
            res = self.n2s(res)
            print(res)
            res = self.s2n(res)

        return res[::-1]
