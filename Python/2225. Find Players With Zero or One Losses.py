class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        l = Counter()
        for i, j in matches:
            l[j] += 1
            if i not in l: l[i] = 0
        return [sorted([x for x, y in l.items() if y == 0]), sorted([x for x, y in l.items() if y == 1])]
