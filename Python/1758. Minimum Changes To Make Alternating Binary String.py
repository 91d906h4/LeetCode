class Solution:
    def minOperations(self, s: str) -> int:
        def dif(s1, s2): return len([a for a, b in zip(s1, s2) if a != b])
        string = "01" * (len(s) // 2)
        return min(dif(string, s), dif("1" + string[:-1], s)) if len(string) == len(s) else min(dif(string + "0", s), dif("1" + string, s))
