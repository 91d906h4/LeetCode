class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        i, j = 0, 1
        while j < len(s):
            if s[i] == s[j]:
                j += 1
            else:
                if j - i >= 3:
                    result.append([i, j - 1])
                i = j
                j += 1
        if j - i >= 3:
            result.append([i, j - 1])
        return result
