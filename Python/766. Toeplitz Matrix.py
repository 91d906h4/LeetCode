class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        temp = matrix[0]
        for i in matrix[1:]:
            if i[1:] != temp[:-1]: return False
            temp = i
        return True
