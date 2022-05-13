class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        temp = []
        for i in rectangles:
            temp.append(min(i[0], i[1]))
        temp.sort(reverse=True)
        return temp.count(temp[0])
