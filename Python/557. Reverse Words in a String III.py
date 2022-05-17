class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        for i in range(len(temp)):
            temp[i] = "".join(reversed(list(temp[i])))
        return " ".join(temp)
