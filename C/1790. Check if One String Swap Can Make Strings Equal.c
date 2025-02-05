bool areAlmostEqual(char* s1, char* s2) {
    int times = 0;
    char r1, r2;

    while (*s1) {
        if (*s1 != *s2) {
            if (times == 0) {
                r1 = *s1;
                r2 = *s2;
                times++;
            } else if (times == 1) {
                if (*s1 == r2 && *s2 == r1)
                    times++;
                else
                    return false;
            } else {
                return false;
            }
        }

        s1++; s2++;
    }

    return times == 0 || times == 2;
}
