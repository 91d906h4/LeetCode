class Solution {
public:
    int bestClosingTime(string customers) {
        customers = "X" + customers;
        int y = 0, n = 0, r = 0, m = 100001;

        for (char i: customers) {
            if (i == 'Y') y++;
        }

        for (int i = 0; i < customers.length(); i++) {
            if (customers[i] == 'Y') y--;
            else n++;

            if (n + y < m) m = n + y, r = i;
        }

        return r;
    }
};
