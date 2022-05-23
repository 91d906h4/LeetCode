class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        temp = Counter(words[0])
        for i in words:
            for j in temp:
                if j not in i:
                    temp[j] = 0
                else:
                    temp[j] = min(temp[j], Counter(i)[j])
        return "".join([a * b for a, b in temp.items() if b != 0])
