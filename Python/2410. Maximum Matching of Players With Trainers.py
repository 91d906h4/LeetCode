class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        res = 0

        players.sort()
        trainers.sort()

        i, j = 0, 0
        lp, lt = len(players), len(trainers)

        while i < lp and j < lt:
            if players[i] <= trainers[j]: i += 1; res += 1
            j += 1

        return res
