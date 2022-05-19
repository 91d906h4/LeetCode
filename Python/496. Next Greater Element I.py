class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        size2 = len(nums2)
        for i in nums1:
            for j in range(nums2.index(i), size2):
                if nums2[j] > i:
                    result.append(nums2[j])
                    break
                elif j == size2 - 1:
                    result.append(-1)
        return result
