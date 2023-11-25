class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {}

        for [i, j] in knowledge:
            d[i] = j

        s = s.split(")")
        r = ""

        for i in s:
            if "(" in i:
                a, b = i.split("(")
                if b in d: b = d[b]
                else: b = "?"
                r += a + b
            else: r += i

        return r
