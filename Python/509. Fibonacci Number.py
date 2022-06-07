class Solution:
    def fib(self, n: int) -> int:
#         def fib(n):
#             if n == 0 or n == 1: return n
#             return fib(n - 1) + fib(n - 2)
#         return fib(n)

        fib = [0, 1]
        for i in range(1, n + 1):
            fib.append(fib[i] + fib[i - 1])
        return fib[n]
