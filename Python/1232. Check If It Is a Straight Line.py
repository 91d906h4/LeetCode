class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]
        m, n = x2 - x1, y2 - y1
        for i in range(len(coordinates) - 1):
            if n * (coordinates[i][0] - coordinates[i + 1][0]) \
            != m * (coordinates[i][1] - coordinates[i + 1][1]): return False
        return True
