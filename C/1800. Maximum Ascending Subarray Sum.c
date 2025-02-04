int max(int a, int b) {
    return a > b ? a : b;
}

int maxAscendingSum(int* nums, int numsSize) {
    int counter = *nums, result = 0;

    for (int* i = nums + 1; i < nums + numsSize; i++) {
        if (*(i - 1) < *i) {
            counter += *i;
        } else {
            result = max(result, counter);
            counter = *i;
        }
    }

    result = max(result, counter);

    return result;
}
