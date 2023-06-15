# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length, peak, res = mountain_arr.length(), 0, -1

        # Find peak.
        l, r = 0, length - 1
        while l <= r:
            peak = (l + r) // 2

            if peak == 0: a = -1
            else: a = mountain_arr.get(peak - 1)
            b = mountain_arr.get(peak)
            if peak == length: c = 1000000001
            else: c = mountain_arr.get(peak + 1)

            if a < b and b > c: break
            elif a < b and b < c: l = peak + 1
            elif a > b and b > c: r = peak - 1

        # Find target in left.
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2

            a = mountain_arr.get(m)
            if a == target:
                res = m
                break
            elif a < target: l = m + 1
            elif a > target: r = m - 1

        if res != -1: return res

        # Find target in right.
        l, r = peak, length
        while l <= r:
            m = (l + r) // 2
            if m >= length: return -1
            a = mountain_arr.get(m)

            if a == target:
                if m < res or res == -1: res = m
                break
            elif a > target: l = m + 1
            elif a < target: r = m - 1

        return res
