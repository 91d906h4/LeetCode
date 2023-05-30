class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        return sum([int(x) for x in n[::2]]) - sum([int(x) for x in n[1::2]])
