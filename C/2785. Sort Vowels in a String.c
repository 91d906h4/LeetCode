#define isVowel(a) ( \
    a == 'A' || a == 'E' || a == 'I' || a == 'O' || a == 'U' || \
    a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u' \
)

compare (a, b)
char* a;
char* b;
{
    return (*a == *b) ? 0 : strcmp(a, b);
}

char * sortVowels(char * s){
    int s_len = strlen(s);
    int v_count = 0;
    char *temp = (char *)malloc(sizeof(char) * s_len);

    for (int i = 0; i < s_len; i++)
        if (isVowel(i[s]))
            (v_count++)[temp] = i[s];

    // Return if no or one vowel.
    if (v_count <= 1)
        return s;

    qsort(temp, v_count, sizeof(char), compare);

    v_count = 0;

    for (int i = 0; i < s_len; i++)
        if (isVowel(i[s]))
            i[s] = (v_count++)[temp];

    free(temp);

    return s;
}
