import re
class Solution:
    def countValidWords(self, sentence: str) -> int:
        result = sentence.split()
        counter = 0
        for i in result:
            print(i)
            if re.match(r'^(([a-z]+\-)?[a-z]+)?[\!|\.|\,]?$', i):
                counter += 1
        return counter
