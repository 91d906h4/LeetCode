int findTheWinner(int n, int k) {
    int r = 0;

    for (int i = 1; i <= n; i++)
        r = (r + k) % i;

    return r + 1;

    // int* t = (int*)malloc(sizeof(int) * n);

    // for (int i = 0; i < n; i++)
    //     t[i] = 1;

    // int ptr = 0;

    // // Remove n - 1 elements.
    // for (int i = 0; i < n - 1; i++) {
    //     int c = k;

    //     while (c > 0) {
    //         if (t[ptr] == 1)
    //             c--;

    //         if (c == 0)
    //             t[ptr] = 0;

    //         ptr = (ptr + 1) % n;
    //     }
    // }

    // for (int i = 0; i < n; i++)
    //     if (t[i] == 1)
    //         return i + 1;

    // free(t);

    // return 0;
}
