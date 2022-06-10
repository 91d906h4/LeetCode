class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
#         if m * n != len(original): return []
#         result = []
#         for i in range(m):
#             temp = []
#             for j in range(n):
#                 temp.append(original.pop(0))
#             result.append(temp)
#         return result

        if m * n != len(original): return []
        result, temp = [], 0
        for i in range(n, len(original) + 1, n):
            result.append(original[temp:i])
            temp = i
        return result
