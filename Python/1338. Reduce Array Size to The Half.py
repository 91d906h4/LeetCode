class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        temp = Counter(arr)
        h, res = len(arr) // 2, 0

        for i in sorted(temp.values(), reverse = True):
            if h > 0:
                res += 1
                h -= i
            else: break

        return res
