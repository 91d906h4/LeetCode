class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def leap(year: int) -> int:
            return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

        if date1 > date2: date1, date2 = date2, date1

        y1, m1, d1 = map(int, date1.split("-"))
        y2, m2, d2 = map(int, date2.split("-"))

        res = 0

        for y in range(y1, y2): res += 365 + leap(y)

        mon[1] = 29 if leap(y1) else 28
        res -= sum(mon[:m1 - 1]) + d1
        mon[1] = 29 if leap(y2) else 28
        res += sum(mon[:m2 - 1]) + d2

        return res
