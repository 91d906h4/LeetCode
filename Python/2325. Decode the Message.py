class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
#         key = key.replace(" ", "")
#         dict_, i = {" ": " "}, 0
#         while len(key) > 0:
#             if key[0] not in dict_.keys():
#                 dict_[key[0]] = chr(i + 97)
#                 i += 1
#             key = key[1:]
#         result = ""
#         for i in message:
#             result += dict_[i]
#         return result

        dict_, temp = {" ": " "}, ord('a')
        for i in key:
            if i not in dict_:
                dict_[i] = chr(temp)
                temp += 1
        result = ""
        for i in message:
            result += dict_[i]
        return result
