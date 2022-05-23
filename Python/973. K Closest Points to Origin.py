class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         return sorted(points, key = lambda a: sqrt(pow(a[0], 2) + pow(a[1], 2)))[:k]

        return sorted(points, key = lambda a: pow(a[0], 2) + pow(a[1], 2))[:k]
