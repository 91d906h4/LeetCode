class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        counter = 0
        for i in words:
            if s.startswith(i):
                counter += 1
        return counter
