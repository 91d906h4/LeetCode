class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customers = "X" + customers
        y, n = customers.count("Y"), 0
        r, m = 0, float("inf")

        for i, x in enumerate(customers):
            if x == "Y": y -= 1
            elif x == "N": n += 1

            if y + n < m: m = y + n; r = i

        return r
