/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getSumAbsoluteDifferences(int* nums, int numsSize, int* returnSize){
    *returnSize = numsSize;

    int* result = (int*)malloc(numsSize * sizeof(int));
    int l = 0, r = 0, temp;

    for (int i = 0; i < numsSize; i++) r += *(nums + i);

    for (int i = 0; i < numsSize; i++) {
        temp = *(nums + i);
        r -= temp;
        *(result + i) = temp * i - l + r - temp * (numsSize - i - 1);
        l += temp;
    }

    return result;
}
