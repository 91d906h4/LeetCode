class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = Counter()
        for i, j in enumerate(list1):
            if j in list2: d[j] += i
        for i, j in enumerate(list2):
            if j in list1: d[j] += i
        d = sorted(d.items(), key = lambda x: x[1])
        t, r = d[0][1], []
        for i, j in d:
            if j == t: r.append(i)
            else: break
        return r
