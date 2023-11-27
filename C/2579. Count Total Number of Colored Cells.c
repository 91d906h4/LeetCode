long long coloredCells(int n) {
    /*
    * a(n) = a(n - 1) + 4 * (n - 1)
    * a(1) = 1
    * a(2) = 5
    * 
    * a(n) = 1 - 2 * n + 2 * n * n
    */

    long long x = n;

    return 1 + 2 * x * (x - 1);
}
