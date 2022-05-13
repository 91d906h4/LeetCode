class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        temp = 0
        for i in arr:
            if i % 2 == 1: temp += 1
            else: temp = 0
            if temp == 3: return True
        return False
