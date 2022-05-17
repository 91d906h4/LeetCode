class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dict_ = {}
        for i in arr:
#             if i not in dict_: dict_[i] = 1
#             else: dict_[i] += 1
            dict_[i] = dict_.get(i, 0) + 1
        temp = [x for x, y in dict_.items() if y == 1]
        if len(temp) >= k: return temp[k-1]
        else: return ""
