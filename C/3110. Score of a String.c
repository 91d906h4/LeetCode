int scoreOfString(char* s) {
    int result = 0;
    int slen = strlen(s);

    for (int i = 1; i < slen; i++)
        result += abs(s[i - 1] - s[i]);

    return result;
}
