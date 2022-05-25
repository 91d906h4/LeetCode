class Solution:
    def findLucky(self, arr: List[int]) -> int:
        temp = Counter(arr)
        temp = sorted(temp.items(), reverse = True)
        for i, j in temp:
            if i == j: return i
        return -1
