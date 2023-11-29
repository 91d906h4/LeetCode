int mySqrt(int x) {
    if (x == 1) return 1;

    long long i = 0, j = x / 2;

    while (i <= j) {
        long long m = (i + j) / 2;
        long long t = m * m;

        if (t == x) return m;
        else if (t > x) j = m - 1;
        else i = m + 1;
    }

    return j;
}
