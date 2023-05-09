class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x, y = len(matrix), len(matrix[0])
        d = 0
        i, j = 0, 0
        t = x * y
        x1, y1 = 0, 0
        res = []

        while t:
            res.append(matrix[i][j])

            if d == 0:
                if j + 1 < y: j += 1
                else: d = 1; i += 1
            elif d == 1:
                if i + 1 < x: i += 1
                else: d = 2; j -= 1
            elif d == 2:
                if j - 1 >= y1: j -= 1
                else:
                    d = 3; i -= 1
                    x1 += 1; y1 += 1
                    x -= 1; y -= 1
            elif d == 3:
                if i - 1 >= x1: i -= 1
                else: d = 0; j += 1

            t -= 1
        
        return res
