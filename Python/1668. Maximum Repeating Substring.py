class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        temp, counter = word, 0
        while sequence.find(word) != -1:
            word += temp
            counter += 1
        return counter
