class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
#         temp = np.rot90(grid)
#         res = 0

#         for i in grid:
#             for j in temp:
#                 if list(i) == list(j): res += 1

#         return res

        temp1 = [repr(x) for x in grid]
        temp2 = []
        for x in range(len(grid)):
            t = []
            for y in range(len(grid[x])):
                t.append(grid[y][x])
            temp2.append(repr(t))
        temp1 = dict(Counter(temp1))
        temp2 = dict(Counter(temp2))
        result = 0
        for i, j in temp1.items():
            result += j * temp2[i] if i in temp2 else 0
        return result
