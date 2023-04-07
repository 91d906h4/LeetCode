class Solution {
public:
    int strStr(string haystack, string needle) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);

        if (haystack.size() < needle.size()) return -1;
        if (haystack == needle) return 0;
        if (haystack.size() < needle.size()) return -1;

        return haystack.find(needle);
    }
};
