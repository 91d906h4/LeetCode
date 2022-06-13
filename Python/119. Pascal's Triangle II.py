class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
#         if rowIndex == 0: return [1]
#         temp = [1, 1]
#         for i in range(2, rowIndex + 1):
#             hoge = [0] * (i - 1)
#             for i in range(len(temp) - 1):
#                 hoge[i] = temp[i] + temp[i + 1]
#             temp = [1] + hoge + [1]
#         return temp

        if rowIndex == 0: return [1]
        temp = [1]
        for i in range(2, rowIndex + 1):
            temp.insert(0, 1)
            for j in range(i - 1):
                temp[j] += temp[j + 1]
        temp.insert(0, 1)
        return temp
