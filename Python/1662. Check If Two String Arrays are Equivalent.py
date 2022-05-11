class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if str("".join(word1)) == str("".join(word2)): return True
        else: return False
