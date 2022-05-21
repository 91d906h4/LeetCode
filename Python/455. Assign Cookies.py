class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, counter = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                counter += 1
                i += 1
            j += 1
        return counter
