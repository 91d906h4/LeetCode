class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = 0
        for i, j in zip_longest(reversed(str(bin(x))[2:]), reversed(str(bin(y))[2:]), fillvalue = 0):
            if str(i) != str(j): temp += 1
        return temp
