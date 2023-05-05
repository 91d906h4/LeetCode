class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        p1, p2 = 0, 0

        for i in range(len(player1)):
            if i - 1 >= 0 and player1[i - 1] == 10: p1 += 2 * player1[i]
            elif i - 2 >= 0 and player1[i - 2] == 10: p1 += 2 * player1[i]
            else: p1 += player1[i]

            if i - 1 >= 0 and player2[i - 1] == 10: p2 += 2 * player2[i]
            elif i - 2 >= 0 and player2[i - 2] == 10: p2 += 2 * player2[i]
            else: p2 += player2[i]

        if p1 == p2: return 0
        return 1 if p1 > p2 else 2
