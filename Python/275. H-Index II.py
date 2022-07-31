class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        t = 0
        for i in citations:
            if i > t: t += 1
            else: break
        return t
