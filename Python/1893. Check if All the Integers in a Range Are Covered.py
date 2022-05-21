class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in [x for x in range(left, right + 1)]:
            temp = 0
            for j in ranges:
                temp += 1
                if j[0] <= i and i <= j[1]: break
                elif temp == len(ranges): return False
        return True
