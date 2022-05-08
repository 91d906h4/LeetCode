class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        size = len(nums)
        result = [0] * size
        index_a = 0
        index_b = sum(x < pivot for x in nums)
        index_c = index_b + sum(x == pivot for x in nums)
        for i in nums:
            if i < pivot:
                result[index_a] = i
                index_a += 1
            elif i == pivot:
                result[index_b] = i
                index_b += 1
            elif i > pivot:
                result[index_c] = i
                index_c += 1
        return result
