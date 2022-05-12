class Solution:
    def tribonacci(self, n: int) -> int:
        temp_0 = 0
        temp_1 = 1
        temp_2 = 1
        if n == 0: return 0
        elif n == 1 or n == 2 : return 1
        for i in range(2, n):
            temp_3 = temp_0 + temp_1 + temp_2
            temp_0 = temp_1
            temp_1 = temp_2
            temp_2 = temp_3
        return temp_3
