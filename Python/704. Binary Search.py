class Solution(object):
    def search(self, nums, target):
        high, mid, low = len(nums) - 1, 0, 0
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1
