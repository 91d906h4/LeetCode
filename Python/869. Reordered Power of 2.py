class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        t = Counter(str(n))
        i = 1
        while i <= n * 10:
            if Counter(str(i)) == t: return True
            print(i)
            i *= 2
        return False
