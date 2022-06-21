class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result = []
        for i in range(len(matrix[0])):
            temp, r = 0, 0
            for j in range(len(matrix)):
                if matrix[j][i] > temp:
                    temp = matrix[j][i]
                    r = j
            if matrix[r][i] == min(matrix[r]): result.append(matrix[r][i])
        return result
