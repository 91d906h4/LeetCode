class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rx1, ry1, rx2, ry2 = rec1
        cx1, cy1, cx2, cy2 = rec2
        return rx1 < cx2 and cx1 < rx2 and ry1 < cy2 and cy1 < ry2
