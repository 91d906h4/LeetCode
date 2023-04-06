class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res, d = [[]], [{}]

        for i in nums:
            trig = True
            for di, j in enumerate(d):
                if i not in j:
                    res[di].append(i)
                    d[di][i] = 1
                    trig = False
                    break

            if trig:
                res.append([i])
                d.append({i: 1})

        return res
