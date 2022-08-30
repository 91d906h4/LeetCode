class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        t = Counter()
        for i, j in items1:
            t[i] += j
        for i, j in items2:
            t[i] += j
        return sorted(t.items())
