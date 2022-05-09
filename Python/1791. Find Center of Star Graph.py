import numpy as np
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
#         a = [0] * 100001
#         for i in edges:
#             a[i[0]] += 1
#             a[i[1]] += 1
#         return a.index(np.amax(a))

        result = {}
        for i in edges:
            if result.get(i[0]):
                result[i[0]] += 1
            else:
                result[i[0]] = 1
            if result.get(i[1]):
                result[i[1]] += 1
            else:
                result[i[1]] = 1
        return max(result, key=result.get)
