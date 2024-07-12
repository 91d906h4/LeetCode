int minimizedStringLength(char * s){
    // Use array of size 256 instead of 26 to reduce the
    // latency of subtraction.
    int table[256] = {0};
    int result = 0, slen = strlen(s);

    for (register int i = 0; i < slen; i++) {
        if (table[(int)s[i]] == 0) {
            table[(int)s[i]] = 1;
            result++;
        }
    }

    return result;
}
