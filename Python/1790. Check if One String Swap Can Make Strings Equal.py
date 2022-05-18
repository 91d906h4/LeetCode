class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
#         size = len(s1)
#         for i in range(size):
#             for j in range(i, size):
#                 temp = list(s1)
#                 temp[i], temp[j] = temp[j], temp[i]
#                 if "".join(temp) == s2: return True
#         return False

        temp = [i for i in range(len(s1)) if s1[i] != s2[i]]
        len_ = len(temp)
        if len_ == 0: return True
        elif len_ == 2:
            if s1[temp[0]] == s2[temp[1]] and s1[temp[1]] == s2[temp[0]]: return True
            else: return False
        else: return False
