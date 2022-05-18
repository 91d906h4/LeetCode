class Solution:
    def isHappy(self, n: int) -> bool:
        dict_ = {}
        while n != 1:
            dict_[n] = 1
            n = list(str(n))
            temp = 0
            for i in n:
                temp += pow(int(i), 2)
            n = int(temp)
            if dict_.get(n, 0) == 1: return False
        return True
