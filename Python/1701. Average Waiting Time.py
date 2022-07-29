class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        result = 0
        temp = customers[0][0]
        for i, j in customers:
            if temp >= i:
                temp += j
            else:
                temp = i + j
            result += temp - i
        return result / len(customers)
