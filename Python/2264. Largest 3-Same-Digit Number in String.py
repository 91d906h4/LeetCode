class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_num = ["999", "888", "777", "666", '555', "444", "333", "222", "111", "000"]
        for i in good_num:
            if num.find(i) != -1:
                return str(i)
        return ""
