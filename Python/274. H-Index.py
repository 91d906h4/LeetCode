class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        m = 0
        for i in range(0, len(citations)):
            if i + 1 <= citations[i]: m = i + 1
        return m
