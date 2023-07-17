int sumOfSquares(int* nums, int numsSize){
    int res = 0;

    for (int i = 0; i < numsSize; i++) {
        if (numsSize % (i + 1) == 0) res += *(nums + i) * *(nums + i);
    }

    return res;
}
