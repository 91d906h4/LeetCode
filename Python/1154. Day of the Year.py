class Solution:
    def dayOfYear(self, date: str) -> int:
        n = 28
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: n = 29
        dict_ = {1: 31, 2: n, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        result = 0
        for i in range(1, month):
            result += dict_[i]
        result += day
        return result
