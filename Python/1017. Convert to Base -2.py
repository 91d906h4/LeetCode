class Solution:
    def baseNeg2(self, n: int) -> str:
        def n_base_k(n, k):
            if n == 0:
                return "0"
            else:
                result = []
                while n != 0:
                    n, i = divmod(n, k)
                    if i < 0:
                        n, i = n + 1, i + 2
                    result.append(str(i))
                return "".join(result)[::-1]
        
        return n_base_k(n, -2)
