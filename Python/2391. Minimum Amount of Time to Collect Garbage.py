class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m, p, g = 0, 0, 0
        for i in range(len(garbage)):
            temp = garbage[i]
            if "M" in temp: m = i
            if "P" in temp: g = i
            if "G" in temp: p = i
        
        garbage = ''.join(garbage)
        
        return sum(travel[:m]) + sum(travel[:p]) + sum(travel[:g]) + garbage.count("M") + garbage.count("P") + garbage.count("G")
