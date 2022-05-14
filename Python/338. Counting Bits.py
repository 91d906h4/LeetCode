class Solution:
    def countBits(self, n: int) -> List[int]:
#         result = []
#         for i in range(n + 1):
#             result.append(list("{:b}".format(i)).count("1"))
#         return result

        return [bin(x).count("1") for x in range(n+1)]
