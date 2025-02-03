int max(int a, int b) {
    return (a > b) ? a : b;
}

int longestMonotonicSubarray(int* nums, int numsSize) {
    int order = 0, result = 0, temp = 1;

    for (int* i = nums + 1; i < nums + numsSize; i++) {
        if (order != -1 && *(i - 1) < *(i)) {
            order = 1;
        } else if (order != 1 && *(i - 1) > *(i)) {
            order = -1;
        } else {
            order *= -1;
            result = max(result, temp);
            temp = *(i - 1) == *(i) ? 0 : 1;
        }
        temp++;
    }

    return max(result, temp);
}
