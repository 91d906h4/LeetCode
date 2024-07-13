int minOperations(int* nums, int numsSize, int k) {
    int temp = k, result = 0;

    for (int i = 0; i < numsSize; i++)
        temp ^= nums[i];

    while (temp != 0) {
        result += temp % 2;
        temp >>= 1;
    }

    return result;
}
