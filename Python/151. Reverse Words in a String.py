class Solution:
    def reverseWords(self, s: str) -> str:
#         result = s.split()
#         result.reverse()
#         result = " ".join(result)
#         return result

        return " ".join(reversed(s.split()))
