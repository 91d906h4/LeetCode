import numpy as np
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a = [0] * 100001
        for i in edges:
            a[i[0]] += 1
            a[i[1]] += 1
        
        return a.index(np.amax(a))
