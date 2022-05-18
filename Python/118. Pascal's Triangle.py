class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
#         result = [[1]]
#         for i in range(1, numRows):
#             temp = [1]
#             for j in range(1, len(result[i - 1])):
#                 temp.append(result[i - 1][j] + result[i - 1][j - 1])
#             temp.append(1)
#             result.append(temp)
#         return result

        result = []
        for i in range(numRows):
            temp = []
            for j in range(i + 1):
                if j == 0 or j == i: temp.append(1)
                else: temp.append(result[i - 1][j] + result[i - 1][j - 1])
            result.append(temp)
        return result
