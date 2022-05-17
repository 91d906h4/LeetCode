class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def helper(number: int) -> int:
            temp = 0
            while number:
                temp += number % 10
                number //= 10
            return temp

        dict_ = {}
        for i in range(lowLimit, highLimit + 1):
#             temp = sum(map(int, list(str(i))))
            temp = helper(i)
            if temp not in dict_:
                dict_[temp] = 1
            else:
                dict_[temp] += 1
        return max(dict_.values())
