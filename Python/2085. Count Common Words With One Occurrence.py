class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a, b = Counter(words1), Counter(words2)
        result = 0
        for i, j in a.items():
            if j != 1: continue
            if b[i] == 1: result += 1
        return result
