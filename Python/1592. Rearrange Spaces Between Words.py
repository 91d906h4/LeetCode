class Solution:
    def reorderSpaces(self, text: str) -> str:
#         s = text.count(" ")
#         text = text.split()
#         temp = len(text) - 1
#         n = s // temp if temp > 0 else 0
#         m = s % temp if temp > 0 else s
#         return (" " * n).join(text) + " " * m

        return (" " * (text.count(" ") // (len(text.split()) - 1) if len(text.split()) - 1 > 0 else 0)).join(text.split()) + " " * (text.count(" ") % (len(text.split()) - 1) if len(text.split()) - 1 > 0 else text.count(" "))
