class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # temp = [[a, b] for a, b in points if a == x or b == y]
        # result = min(temp, key = lambda n: abs(n[0] - x) + abs(n[1] - y), default = None)
        # return points.index(result) if result else -1
        
        index_, temp = -1, inf
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                n = abs(a - x) + abs(b - y)
                if n < temp:
                    temp = n
                    index_ = i
        return index_
