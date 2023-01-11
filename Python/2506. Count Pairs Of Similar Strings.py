class Solution:
    def similarPairs(self, words: List[str]) -> int:
        return sum([x * (x - 1) // 2 for x in Counter(repr(set(sorted(x))) for x in words).values()])
