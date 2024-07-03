int lengthOfLongestSubstring(char* s) {
    int table[128], i = 0, temp = 0, result = 0;

    memset(table, -1, sizeof(table));

    while (*(s + i) != '\0') {
        if (*(table + (int)*(s + i)) == -1) {
            *(table + (int)*(s + i)) = i;
            temp++;
            i++;
        } else {
            result = result > temp ? result : temp;
            i = *(table + (int)*(s + i)) + 1;
            temp = 0;
            memset(table, -1, sizeof(table));
        }
    }

    result = result > temp ? result : temp;

    return result;
}
