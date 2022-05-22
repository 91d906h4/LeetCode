class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        h, w = len(board), len(board[0])
        def dfs(x, y):
            if not 0 <= x < h or not 0 <= y < w or (x, y) in temp: return
            temp.add((x, y))
            if board[x][y] == "X":
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
        
        temp = set()
        result = 0
        for i in range(h):
            for j in range(w):
                if board[i][j] == "X" and (i, j) not in temp:
                    dfs(i, j)
                    result += 1
        return result
