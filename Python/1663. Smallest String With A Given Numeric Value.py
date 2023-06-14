class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n

        temp = [1 for _ in range(n)]

        while k > 0:
            n -= 1
            
            if k >= 25:
                temp[n] += 25
                k -= 25
            else:
                temp[n] += k
                k = 0

        return "".join((chr(x + 96) for x in temp))
