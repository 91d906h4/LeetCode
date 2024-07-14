class Solution:
    def largestPalindromic(self, num: str) -> str:
        table = {}
        result = ""

        for c in num:
            if c in table: table[c] += 1
            else: table[c] = 1

        for i in "987654321":
            if i in table and table[i] >= 2:
                result += i * (table[i] // 2)
                table[i] %= 2

        if result != "" and "0" in table:
            result += "0" * (table["0"] // 2)
            table["0"] %= 2

        t_ = False

        for i in "9876543210":
            if i in table and table[i] != 0:
                result = result + i + result[::-1]
                t_ = True
                break

        if not t_:
            result = result + result[::-1]

        return result
