int minOperations(int* nums, int numsSize, int k) {
    int result = 0;

    for (int i = 0; i < numsSize; i++)
        if (nums[i] < k)
            result++;

    return result;
}
