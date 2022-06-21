class Solution:
    def reorderSpaces(self, text: str) -> str:
        s = text.count(" ")
        text = text.split()
        temp = len(text) - 1
        n = s // (temp) if temp > 0 else 0
        m = s % (temp) if temp > 0 else s
        return (" " * n).join(text) + " " * m
