class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
#         res, temp = 0, {}

#         for i in nums:
#             a, b = str(i), str(int(str(i)[::-1]))

#             if a not in temp:
#                 temp[a] = 1
#                 res += 1
#             if b not in temp:
#                 temp[b] = 1
#                 res += 1

#         return res

        temp = set()

        for i in nums:
            temp.add(i)
            temp.add(int(str(i)[::-1]))

        return len(temp)
