double pow_(double x, long long n) {
    if (n == 0) return 1;
    if (n < 0) return 1.0 / pow(x, n * -1);

    if (n % 2) return x * pow(x * x, n / 2);
    else return pow(x * x, n / 2);
}

double myPow(double x, int n){
    return pow_(x, (long long)n);
}
