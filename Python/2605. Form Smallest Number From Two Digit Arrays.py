class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if set(nums1) & set(nums2) != set(): return min(set(nums1) & set(nums2))
        a, b = min(nums1), min(nums2)
        return int(str(a) + str(b)) if a < b else int(str(b) + str(a))
