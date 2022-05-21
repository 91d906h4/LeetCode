class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = sorted(score, reverse = True)
        result = {}
        for i in range(0, len(temp)):
            if i == 0: k = "Gold Medal"
            elif i == 1: k = "Silver Medal"
            elif i == 2: k = "Bronze Medal"
            else: k = str(i + 1)
            result[temp[i]] = k
        rank = []
        for i in score:
            rank.append(result[i])
        return rank
