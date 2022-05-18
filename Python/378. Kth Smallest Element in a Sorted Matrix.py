class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         return sorted(sum(matrix, []))[k - 1]
#         return sorted([i for j in matrix for i in j])[k - 1]
        return sorted(itertools.chain.from_iterable(matrix))[k - 1]
