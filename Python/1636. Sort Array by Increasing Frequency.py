class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
#         temp = sorted(Counter(nums).items(), key = lambda x: (x[1], x[0] * -1))
#         r = []
#         for i, j in temp:
#             r += [i] * j
#         return r

        return sum([[i] * j for i, j in sorted(Counter(nums).items(), key = lambda x: (x[1], x[0] * -1))], [])
