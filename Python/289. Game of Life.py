class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        temp = deepcopy(board)
        rl, cl = len(board), len(board[0])

        for i in range(rl):
            for j in range(cl):
                neb = 0

                if i - 1 >= 0: neb += board[i - 1][j]
                if j - 1 >= 0: neb += board[i][j - 1]
                if i + 1 < rl: neb += board[i + 1][j]
                if j + 1 < cl: neb += board[i][j + 1]
                if i - 1 >= 0 and j - 1 >= 0: neb += board[i - 1][j - 1]
                if i - 1 >= 0 and j + 1 < cl: neb += board[i - 1][j + 1]
                if i + 1 < rl and j - 1 >= 0: neb += board[i + 1][j - 1]
                if i + 1 < rl and j + 1 < cl: neb += board[i + 1][j + 1]

                if neb < 2 or neb > 3: temp[i][j] = 0
                elif neb == 2: temp[i][j] = board[i][j]
                elif neb == 3: temp[i][j] = 1

        for i in range(rl):
            for j in range(cl):
                board[i][j] = temp[i][j]
