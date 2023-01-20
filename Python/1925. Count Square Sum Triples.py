class Solution:
    def countTriples(self, n: int) -> int:
        res = 0

        for i in range(1, n):
            for j in range(1, n):
                temp = (i * i + j * j) ** 0.5
                if temp <= n and temp.is_integer(): res += 1
        
        return res
