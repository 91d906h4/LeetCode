class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        a, b = startPos[0], homePos[0]
        c, d = startPos[1], homePos[1]

        if a > b: a, b = b, a
        else: a, b = a + 1, b + 1

        if c > d: c, d = d, c
        else: c, d = c + 1, d + 1

        return sum(rowCosts[a:b]) + sum(colCosts[c:d])
