class Solution:
    def sortString(self, s: str) -> str:
#         dict_ = {}
#         for i in s:
#             if i not in dict_: dict_[i] = 1
#             else: dict_[i] += 1
#         result = []
#         dict_ = sorted(dict_.items())
#         dict_ = dict((x, y) for x, y in dict_)
#         x = 0
#         while x < len(s):
#             if x % 2 == 0:
#                 for i, j in enumerate(dict_):
#                     if dict_[j] > 0:
#                         result.append(j)
#                         dict_[j] -= 1
#             else:
#                 for i, j in enumerate(reversed(dict_)):
#                     if dict_[j] > 0:
#                         result.append(j)
#                         dict_[j] -= 1
#             x += 1
#         return "".join(result)

        dict_ = dict(Counter(s))
        char = sorted(dict_.keys())
        result = ""
        while len(result) < len(s):
            for i in char:
                if dict_[i] > 0:
                    result += i
                    dict_[i] -= 1
            for i in char[::-1]:
                if dict_[i] > 0:
                    result += i
                    dict_[i] -= 1
        return result
