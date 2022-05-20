class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # return [x for x in range(1, max(arr) + k + 1) if x not in arr][k - 1]

        # for j in arr:
        #     if j <= k: k += 1
        #     else: break
        # return k
        
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] - (m + 1) < k:
                l = m + 1
            else:
                r = m
        return l + k
