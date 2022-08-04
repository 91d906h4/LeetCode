class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if len(set(map(repr, [p1, p2, p3, p4]))) != 4: return False
        def helper(a, b):
            return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
        
        a, b, c, d, e, f = helper(p1, p2), helper(p1, p3), helper(p1, p4), helper(p2, p3), helper(p2, p4), helper(p3, p4)
        r = [a, b, c, d, e, f]
        t = set(r)
        if len(t) != 2: return False
        for i in t:
            if r.count(i) not in [2, 4]: return False
        return True
