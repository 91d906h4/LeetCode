class Solution:
    def canPlaceFlowers(self, flowered: List[int], n: int) -> bool:
#         for i, element in enumerate(flowered):
#             if element == 0 and (i == 0 or flowered[i - 1] == 0) and (i == len(flowered) - 1 or flowered[i + 1] == 0):
#                 flowered[i] = 1
#                 n -= 1
#             if n <= 0:
#                 return True
#         return False

        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

        return n <= 0
