bool isPowerOfFour(int n){
    if (n == 1) return 1;
    if (n % 2 || n < 0) return 0;

    long long i = 1;

    while (i < n) i *= 4;

    return i == n;
}
