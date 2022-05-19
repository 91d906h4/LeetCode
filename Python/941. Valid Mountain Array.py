class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
#         max_ = max(arr)
#         mountain = arr.index(max_)
#         if len(arr) <= 2 or mountain == 0 or mountain == len(arr) - 1: return False
#         temp = -1
#         for i in range(mountain):
#             if arr[i] <= temp: return False
#             else: temp = arr[i]
#         temp = max_
#         for i in range(mountain + 1, len(arr)):
#             if arr[i] >= temp: return False
#             else: temp = arr[i]
#         return True

        if len(arr) < 3: return False
        i = 1
        while i < len(arr) and arr[i - 1] < arr[i]: i += 1
        if i == 1 or i == len(arr): return False
        else:
            while i < len(arr) and arr[i - 1] > arr[i]: i += 1
        return i == len(arr)
