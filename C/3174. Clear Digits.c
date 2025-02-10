bool isAlpha(char c) {
    return 97 <= (int)c && (int)c <= 122;
}

void append(char** s, char c) {
    size_t len = strlen(*s);
    char* new = realloc(*s, len + 2);

    new[len] = c;
    new[len + 1] = '\0';

    *s = new;
}

void pop(char** s) {
    size_t len = strlen(*s);

    if (len == 0)
        return;

    char* new = realloc(*s, len);

    new[len - 1] = '\0';
    *s = new;
}

char* clearDigits(const char* s) {
    char* r = malloc(1);

    *r = '\0';

    while (*s) {
        if (isAlpha(*s))
            append(&r, *s);
        else
            pop(&r);

        s++;
    }

    return r;
}
