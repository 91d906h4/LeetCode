class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        r, t, p, l = "", 0, 0, len(spaces)
        for i in s:
            if p < l and t == spaces[p]:
                r += " "
                p += 1
            r += i
            t += 1
        return r
