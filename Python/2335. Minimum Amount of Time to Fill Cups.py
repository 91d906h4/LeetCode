class Solution:
    def fillCups(self, amount: List[int]) -> int:
        res = 0
        c, w, h = amount

        while c > 0 or w > 0 or h > 0:
            m = min(c, w, h)
            
            if m == c:
                w -= 1
                h -= 1
            elif m == w:
                c -= 1
                h -= 1
            elif m == h:
                c -= 1
                w -= 1
            
            res += 1

        return res
