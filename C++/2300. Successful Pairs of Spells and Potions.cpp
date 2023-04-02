class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());

        vector<int> res;
        int length = potions.size();

        for (long long i: spells) {
            int l = 0, r = length - 1, m;

            while (l <= r) {
                m = (l + r) / 2;

                if (potions[m] * i >= success) r = m - 1;
                else l = m + 1;
            }

            if (m == length) res.push_back(0);
            else res.push_back(length - l);
        }

        return res;
    }
};
