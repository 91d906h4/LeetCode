class Solution:
    def findComplement(self, num: int) -> int:
#         return int("".join(["1" if x == "0" else "0" for x in list(str(bin(num)))[2:]]), 2)

        k = 1
        while k < num: k = k * 2 + 1
        return num ^ k
