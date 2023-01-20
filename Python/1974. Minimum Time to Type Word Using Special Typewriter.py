class Solution:
    def minTimeToType(self, word: str) -> int:
        res, word = -1, 'a' + word

        for i in range(len(word) - 1):
            res += min(abs(ord(word[i]) - ord(word[i + 1])), 26 - abs(ord(word[i]) - ord(word[i + 1])))
        
        return res + len(word)
