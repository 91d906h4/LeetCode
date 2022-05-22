class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dict_ = Counter()
        for i in bills:
            if i == 5:
                dict_[5] += 1
            elif i == 10:
                dict_[10] += 1
                dict_[5] -= 1
            elif i == 20:
                dict_[20] += 1
                if dict_[10] > 0:
                    dict_[10] -= 1
                    dict_[5] -= 1
                else:
                    dict_[5] -= 3
            if dict_[5] < 0 or dict_[10] < 0 or dict_[20] < 0: return False
        return True
