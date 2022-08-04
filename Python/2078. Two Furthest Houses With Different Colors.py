class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l = len(colors) - 1
        i, j = 0, l
        while colors[i] == colors[l] and colors[0] == colors[j]:
            i += 1
            j -= 1
        return max(l - i, j - 0)
