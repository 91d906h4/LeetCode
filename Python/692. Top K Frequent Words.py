class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [x for x, _ in sorted(Counter(words).items(), key = lambda x: (-1 * x[1], x[0]))[:k]]
