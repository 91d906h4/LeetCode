class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        recoder = []
        for i in range(0, len(points)):
            recoder.append(points[i][0])
        recoder.sort()
        xmax = 0
        for i in range(0, len(recoder)-2):
            xmax = max(xmax, recoder[i+1] - recoder[i])
        return xmax
