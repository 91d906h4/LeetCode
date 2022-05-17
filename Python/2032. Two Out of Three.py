class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
#         nums1 = list(dict.fromkeys(nums1))
#         nums2 = list(dict.fromkeys(nums2))
#         nums3 = list(dict.fromkeys(nums3))
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums3 = list(set(nums3))
        
        dict_ = {}
        for i, j, k in zip_longest(nums1, nums2, nums3, fillvalue = 0):
            if i not in dict_: dict_[i] = 1
            else: dict_[i] += 1
            if j not in dict_: dict_[j] = 1
            else: dict_[j] += 1
            if k not in dict_: dict_[k] = 1
            else: dict_[k] += 1
        
        return sorted([x for x, y in dict_.items() if y >= 2 and x != 0])
