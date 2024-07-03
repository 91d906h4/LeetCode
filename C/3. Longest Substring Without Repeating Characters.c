int lengthOfLongestSubstring(char* s) {
    int table[128], i = 0, temp = 0, result = 0;

    memset(table, -1, sizeof(table));

    while (*(s + i) != '\0') {
        int* temp_p = table + (int)*(s + i);

        if (*temp_p == -1) {
            *temp_p = i;
            temp++;
            i++;
        } else {
            result = result > temp ? result : temp;
            i = *temp_p + 1;
            temp = 0;
            memset(table, -1, sizeof(table));
        }
    }

    result = result > temp ? result : temp;

    return result;
}
