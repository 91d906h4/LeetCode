class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {x: [] for x in range(9)}
        column = {x: [] for x in range(9)}
        box = {x: [] for x in range(9)}
        
        for i in range(9):
            for j in range(9):
                index_ = (i // 3) * 3 + j // 3
                temp = board[i][j]
                if temp == ".": continue
                elif temp in row[i] or temp in column[j] or temp in box[index_]: return False
                else:
                    row[i].append(temp)
                    column[j].append(temp)
                    box[index_].append(temp)
        return True
