class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # hoge = []
        # for i in range(len(matrix[0])):
        #     fuga = []
        #     for j in range(len(matrix)):
        #         fuga.append(matrix[j][i])
        #     hoge.append(fuga)
        # return hoge
        
        return list(zip(*matrix))
