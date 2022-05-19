class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return sum(matrix, []).count(target) != 0
