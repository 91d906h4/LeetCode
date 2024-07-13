int differenceOfSums(int n, int m) {
    int result = 0;

    for (int i = 1; i <= n; i++)
        result += (i % m != 0) ? i : -i;

    return result;
}
