int findPermutationDifference(char* s, char* t) {
    int table[256];
    int slen = strlen(s);
    int result = 0;

    for (int i = 0; i < 256; i++)
        table[i] = -1;

    for (int i = 0; i < slen; i++) {
        if (table[(int)s[i]] == -1)
            table[(int)s[i]] = i;
        else
            result += abs(i - table[(int)s[i]]);

        if (table[(int)t[i]] == -1)
            table[(int)t[i]] = i;
        else
            result += abs(i - table[(int)t[i]]);
    }

    return result;
}
