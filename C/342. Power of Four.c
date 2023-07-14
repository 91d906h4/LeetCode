bool isPowerOfFour(int n){
    if (n == 1) return 1;
    if (n % 2 || n < 0) return 0;

    for (long long  i = 1; i <= n; i *= 4) {
        if (i == n) return 1;
    }

    return 0;
}
