class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        len_ = len(arr)
        i, j = 0, 0
        for i in range(len_):
            if arr[j] == 0:
                arr.insert(j, 0)
                j += 1
            i += 1
            j += 1
        arr[:] = arr[:len_]
        return arr
