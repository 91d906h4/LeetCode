int maximizeSum(int* nums, int numsSize, int k){
    int m = 0, t = 0;

    for (int i = 0; i < numsSize; i++) m = (*(nums + i) > m) ? *(nums + i) : m;
    for (int i = 1; i < k; i++) t += i;

    return m * k + t;
}
