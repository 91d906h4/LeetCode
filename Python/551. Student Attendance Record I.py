class Solution:
    def checkRecord(self, s: str) -> bool:
#         A, L, temp = 0, 0, 0
#         for i in s:
#             if i == "P":
#                 temp = 0
#             elif i == "A":
#                 A += 1
#                 temp = 0
#             elif i == "L":
#                 temp += 1
#             L = max(L, temp)
#         return A < 2 and L < 3

        return s.count("A") < 2 and "LLL" not in s
