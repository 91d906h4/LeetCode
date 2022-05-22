class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        temp = [[0] * len(colSum) for _ in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                temp[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= temp[i][j]
                colSum[j] -= temp[i][j]
        return temp
