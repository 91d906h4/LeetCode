class Solution:
    def clearDigits(self, s: str) -> str:
        # table = {}

        # for i, c in enumerate(s):
        #     table[i] = c.isalpha()

        # for i, c in enumerate(s):
        #     if not c.isdigit():
        #         continue

        #     for j in range(i - 1, -1, -1):
        #         if table[j]:
        #             table[j] = False
        #             break

        # result = ""

        # for i, c in enumerate(s):
        #     if table[i]:
        #         result += c

        # return result

        result = []

        for c in s:
            if c.isalpha():
                result.append(c)
            else:result.pop()

        return "".join(result)
