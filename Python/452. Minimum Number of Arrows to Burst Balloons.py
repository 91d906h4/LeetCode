class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        
        arrow = 1
        position = points[0][1]

        for [i, j] in points:
            if position < i:
                arrow += 1
                position = j

        return arrow
