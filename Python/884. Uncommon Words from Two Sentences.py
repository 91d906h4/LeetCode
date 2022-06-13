class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
#         a, b = Counter(s1.split()), Counter(s2.split())
#         c1, c2 = list(set(a) - set(b)), list(set(b) - set(a))
#         d = []
#         for i in c1:
#             if a[i] == 1: d.append(i)
#         for j in c2:
#             if b[j] == 1: d.append(j)
#         return d
        
        return [x for x in s1.split() + s2.split() if (s1.split() +s2.split()).count(x) == 1]
