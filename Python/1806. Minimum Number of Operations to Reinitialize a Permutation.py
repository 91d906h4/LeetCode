class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [x for x in range(n)]
        ori = [x for x in range(n)]
        arr = [0] * len(perm)
        result = 0
        while True:
            for i, j in enumerate(perm):
                if i % 2 == 0: arr[i] = perm[i // 2]
                else: arr[i] = perm[n // 2 + (i - 1) // 2]
            if arr == ori: break
            perm = deepcopy(arr)
            arr = [0] * len(perm)
            result += 1
        return result + 1
