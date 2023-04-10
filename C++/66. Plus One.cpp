class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int overflow = 1, temp;

        for (int i = digits.size() - 1; i >= 0; i--) {
            temp = digits[i] + overflow;
            digits[i] = temp % 10;
            overflow = temp / 10;
        }

        if (overflow != 0) digits.insert(digits.begin(), overflow);

        return digits;
    }
};
