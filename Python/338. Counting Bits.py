class Solution:
    # def counter(self, n: int) -> int:
    #     temp, pointer = 0, 131072

    #     while n:
    #         if pointer > n: pointer /= 2
    #         else: n -= pointer; temp += 1

    #     return temp

    def countBits(self, n: int) -> List[int]:
        # return [self.counter(i) for i in range(n + 1)]

        # return [bin(x).count("1") for x in range(n+1)]

        if n == 0: return [0]
        if n == 1: return [0, 1]
        res, t = [0, 1], 0

        for i in range(2, n + 1): res.append(res[i >> 1] + t); t = 1 if not t else 0

        return res
