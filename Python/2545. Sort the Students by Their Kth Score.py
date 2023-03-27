class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        temp = {x: y for x, y in enumerate([score[x][k] for x in range(len(score))])}
        temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
        temp = [x[0] for x in temp]

        res = [[] for _ in range(len(score))]

        for i, x in enumerate(temp): res[i] = score[x]

        return res
