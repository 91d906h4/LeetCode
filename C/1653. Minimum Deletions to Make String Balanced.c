int minimumDeletions(char* s) {
    int b_before = 0, a_after = 0, result = 0;

    int i = 0;
    while (true) {
        if (*(s + i) == 'a')
            a_after++;
        else if (*(s + i) == '\0')
            break;

        i++;
    }

    result = a_after - (*s == 'a' ? 1 : 0);

    i = 0;
    while (true) {
        if (*(s + i) == 'a')
            a_after--;
        else if (*(s + i) == 'b')
            b_before++;
        else
            break;

        if (a_after + b_before < result)
            result = a_after + b_before;

        i++;
    }

    return result;
}
