class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hoge = Counter()
        fuga = 1
        for i in sorted(set(arr)):
            hoge[i] = fuga
            fuga += 1
        return [hoge[x] for x in arr]
