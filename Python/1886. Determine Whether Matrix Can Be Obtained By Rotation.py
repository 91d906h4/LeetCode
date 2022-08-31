class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        l = len(mat)
        def helper(arr):
            t = copy.deepcopy(arr)
            for i in range(l):
                for j in range(l - 1, -1, -1):
                    t[j][i] = arr[i][l - j - 1]
            return t
        
        temp = mat
        for _ in range(4):
            if temp == target: return True
            temp = helper(temp)
        return False
