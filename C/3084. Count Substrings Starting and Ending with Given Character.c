long long countSubstrings(char* s, char c) {
    long long r = 0;

    while (*s != '\0')
        if (*s++ == c) r++;

    return r * (r + 1) / 2;
}
