class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        l = len(creators)
        d1, d2 = {}, {}
        m = 0

        for i in range(l):
            temp = creators[i]
            if temp not in d1:
                d1[temp] = views[i]
                d2[temp] = [views[i], ids[i]]
            else:
                d1[temp] += views[i]

                if views[i] > d2[temp][0] or (views[i] == d2[temp][0] and str(ids[i]) < str(d2[temp][1])):
                    d2[temp] = [views[i], ids[i]]

            m = max(m, d1[temp])

        temp = set()
        res = []

        for i in range(l):
            t = creators[i]
            if d1[t] == m and t not in temp:
                res.append([creators[i], d2[creators[i]][1]])
                temp.add(t)

        return res
