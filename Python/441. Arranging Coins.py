class Solution:
    def arrangeCoins(self, n: int) -> int:
        # k = 1
        # while True:
        #     if n == (k + 1) * k / 2: return k
        #     elif n < (k + 1) * k / 2: return k - 1
        #     k += 1

        # return int((-1 + sqrt(1 + 8 * n)) / 2)

        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            temp = (mid + 1) * mid // 2
            if temp == n:
                return mid
            elif temp > n:
                right = mid - 1
            else:
                left = mid + 1
        return right
