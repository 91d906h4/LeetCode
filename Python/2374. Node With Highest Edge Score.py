class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        temp = {}
        res, c = 0, 0

        for i, x in enumerate(edges):
            if x not in temp: temp[x] = i
            else: temp[x] += i

        t = sorted(temp.keys(), reverse=True)

        for i in t:
            if temp[i] >= c:
                c = temp[i]
                res = i

        return res
