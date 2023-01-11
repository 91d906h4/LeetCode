class Solution:
    def captureForts(self, forts: List[int]) -> int:
        m, res, lock = 0, 0, -2

        for i in forts:
            if i == 0: m += 1
            else:
                if lock == -2: m = 0
                elif lock == i: m = 0
                else:
                    res = max(res, m)
                    m = 0
                lock = i
        
        return res
