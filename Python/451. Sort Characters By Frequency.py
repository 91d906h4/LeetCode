class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([x * y for x, y in sorted(Counter(s).items(), key = lambda t: t[1], reverse = True)])
