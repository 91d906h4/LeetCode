class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib, res = [1, 1], 0

        while fib[-1] < k: fib.append(fib[-2] + fib[-1])

        l = len(fib)
        while k > 0:
            for i in range(l - 1, -1, -1):
                if fib[i] <= k:
                    k -= fib[i]
                    res += 1
                    break

        return res
