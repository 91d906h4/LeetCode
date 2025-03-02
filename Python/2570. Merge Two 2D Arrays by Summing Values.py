class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        t = defaultdict(int)

        for id1, val1 in nums1: t[id1] += val1
        for id2, val2 in nums2: t[id2] += val2

        return sorted(t.items(), key=lambda x: x[0])
