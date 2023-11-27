class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        l = len(str(k))
        r = 0
        i = 0

        while i < len(s):
            if (int(s[i:i+l]) <= k):
                i += l
            else:
                if (l - 1 == 0): return -1
                i += l - 1
            r += 1

        return r
