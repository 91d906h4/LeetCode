class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& arr) {
        int avg = 0, temp = 0, counter = 0;

        for (int i: arr) avg += i;
        if (avg % 3 != 0) return false;
        avg /= 3;

        for (int i: arr) {
            temp += i;
            if (temp == avg) temp = 0, counter++;
        }

        return counter >= 3;
    }
};
