class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        temp = {}

        for i, x in enumerate(s):
            if x not in temp: temp[x] = i
            elif i - temp[x] - 1 != distance[ord(x) - 97]: return False
        
        return True
