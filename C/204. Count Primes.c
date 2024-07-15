int countPrimes(int n) {
    if (n <= 2)
        return 0;

    int table[5000001];
    int result = 1;

    for (int i = 2; i <= n; i++)
        table[i] = (i % 2 == 0);

    for (int i = 3; i < n; i += 2) {
        if (table[i] == 1)
            continue;

        table[i] = 1;
        result++;

        int c = 2;

        while ((i * c) <= n)
            table[i * c++] = 1;
    }

    return result;
}
