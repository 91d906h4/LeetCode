#include <math.h>

bool isPrime(int n) {
    if (n <= 1) return false;

    int temp = sqrt(n);

    for (int i = 2; i <= temp; i++) {
        if (n % i == 0) return false;
    }

    return true;
}
int nonSpecialCount(int l, int r) {
    int result = r - l + 1;

    for (int i = ceil(sqrt(l)); i <= floor(sqrt(r)); i++) {
        if (isPrime(i)) result--;
    }

    return result;
}
