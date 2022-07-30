class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        l = defaultdict(list)
        for i, j in logs:
            if j not in l[i]:
                l[i].append(j)
        result = [0] * k
        for i in l:
            result[len(l[i]) - 1] += 1
        return result
