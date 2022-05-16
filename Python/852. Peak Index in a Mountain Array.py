class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
#       return arr.index(max(arr))

        high, low = len(arr) - 1, 0
        while high > low:
            mid = (high + low) // 2
            if arr[mid] >arr[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low
