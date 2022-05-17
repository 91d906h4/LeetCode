class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
#         def strmun(s: str) -> int:
#             temp = ""
#             for i in list(s):
#                 temp = temp + str(ord(i) - 97)
#             return int(temp)

        def strmun(s: str) -> int:
            temp = 0
            for i in s:
                temp = temp * 10 + ord(i) - 97
            return temp
        return strmun(firstWord) + strmun(secondWord) == strmun(targetWord)
