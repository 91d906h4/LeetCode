class Solution:
    def reverseWords(self, s: str) -> str:
#         temp = s.split()
#         for i in range(len(temp)):
#             temp[i] = "".join(reversed(list(temp[i])))
#         return " ".join(temp)

        s = s[::-1].split()
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return " ".join(s)
