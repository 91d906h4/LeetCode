class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp, res = {}, []

        for i in nums1:
            if i not in temp: temp[i] = 1
            else: temp[i] += 1

        for i in nums2:
            if i in temp and temp[i] > 0:
                res.append(i)
                temp[i] -= 1

        return res
