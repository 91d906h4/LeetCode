class Solution:
    def bitwiseComplement(self, n: int) -> int:
#         return int("".join(["1" if x == "0" else "0" for x in list(str(bin(n)))[2:]]), 2)

        k = 1
        while k < n: k = k * 2 + 1
        return n ^ k
