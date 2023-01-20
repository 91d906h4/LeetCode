class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        l, m, res = len(arr), 10001, []
        
        arr.sort()

        for i in range(l - 1): m = min(m, arr[i + 1] - arr[i])
        for i in range(l - 1):
            if arr[i + 1] - arr[i] == m: res.append([arr[i], arr[i + 1]])
        
        return res
