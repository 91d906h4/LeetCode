class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
#         result, temp = [], []
#         temp = list(set([x for x in nums1 if x not in nums2 and x not in temp]))
#         result.append(temp)
#         temp = list(set([x for x in nums2 if x not in nums1 and x not in temp]))
#         result.append(temp)
#         return result

        temp1, temp2 = set(nums1), set(nums2)
        return [list(temp1 - temp2), list(temp2 - temp1)]
