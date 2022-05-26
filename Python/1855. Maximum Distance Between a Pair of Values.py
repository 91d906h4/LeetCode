class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j, hoge = 0, 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                hoge = max(hoge, j - i)
                j += 1
            else: i += 1
        return hoge
