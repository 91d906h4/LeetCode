class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []

        for x, y, r in queries:
            temp = 0
            for i, j in points:
                if (x - i) ** 2 + (y - j) ** 2 <= r ** 2: temp += 1
            res.append(temp)

        return res
