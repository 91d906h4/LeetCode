class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        horizontalCuts.append(h)
        verticalCuts.append(w)

        ht, wt = 0, 0

        temp = 0
        for i in horizontalCuts:
            if (i - temp > ht): ht = i - temp
            temp = i

        temp = 0
        for i in verticalCuts:
            if (i - temp > wt): wt = i - temp
            temp = i

        temp = (10 ** 9 + 7)
        res = ht * wt

        if res > temp: return res % temp
        else: return res
