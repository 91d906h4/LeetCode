class Solution:
    def arrangeWords(self, text: str) -> str:
        text.lower()
        temp = [[len(x), x] for x in text.split()]
        temp.sort(key = lambda x: x[0])
        return " ".join([x[1] for x in temp]).capitalize()
