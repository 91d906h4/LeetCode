class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        temp = Counter()
        for i, j in logs:
            for n in range(i, j):
                temp[n] += 1
        a = list(temp.most_common())
        a = [x for x in a if x[1] == a[0][1]]
        a.sort()
        print(a)
        return a[0][0]
