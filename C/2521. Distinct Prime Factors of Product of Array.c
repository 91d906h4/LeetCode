void varify(int num, int* prime) {
    for (int i = 2; i <= num; i++) {
        while (num % i == 0) {
            num /= i;
            prime[i] = 1;
        }

        if (num == 1) break;
    }
}

int distinctPrimeFactors(int* nums, int numsSize) {
    int prime[1001] = {0};

    for (int i = 0; i < numsSize; i++) {
        varify(*(nums + i), prime);
    }

    int res = 0;

    for (int i = 0; i < 1001; i++) {
        res += prime[i];
    }

    return res;
}
