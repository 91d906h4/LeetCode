/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int compare(const void* a, const void* b) {
    int int_a = *((int*)a);
    int int_b = *((int*)b);

    if (int_a == int_b) return 0;
    else if (int_a < int_b) return -1;
    else return 1;
}

int* numberGame(int* nums, int numsSize, int* returnSize) {
    qsort(nums, numsSize, sizeof(int), compare);

    for (int i = 0; i < numsSize; i += 2) {
        int temp = nums[i];
        nums[i] = nums[i + 1];
        nums[i + 1] = temp;
    }

    *returnSize = numsSize;

    return nums;
}
