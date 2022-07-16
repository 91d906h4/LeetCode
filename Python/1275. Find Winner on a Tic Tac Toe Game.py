class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        dict_ = {0: 1, 7: 2, 14: 3, 2: 4, 9: 5, 16: 6, 4: 7, 11: 8, 18: 9}
        A, B = set(), set()
        for i in range(len(moves)):
            if i & 1: B.add(dict_[moves[i][0] * 7 + moves[i][1] * 2])
            else: A.add(dict_[moves[i][0] * 7 + moves[i][1] * 2])
        
        temp = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 5, 9}, {3, 5, 7}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}]
        for i in temp:
            if i.issubset(A): return "A"
            elif i.issubset(B): return "B"
        print(A, B)
        return "Draw" if len(moves) == 9 else "Pending"
