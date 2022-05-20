class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # len_ = len(arr)
        # result = []
        # for i in range(len_):
        #     for j in range(i, len_):
        #         if (i + j) % 2 == 0:
        #             result += [arr[i:j + 1]]
        # return sum([sum(x) for x in result])

        len_ = len(arr)
        result = 0
        for i in range(len_):
            result += (((i + 1) * (len_ - i) + 1) // 2) *arr[i]
        return result
