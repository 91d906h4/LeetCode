class Solution {
public:
    string convertToTitle(int columnNumber) {
        string res = "";

        while (columnNumber > 0) {
            printf("%d", columnNumber);
            int temp = columnNumber % 26;

            if (temp == 0) {
                temp = 26;
                columnNumber -= 26;
            }

            res = (char)('A' + temp - 1) + res;

            columnNumber /= 26;
        }

        return res;
    }
};
