class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        for i in sentence:
            if i.startswith(searchWord):
                return sentence.index(i) + 1
        return -1
