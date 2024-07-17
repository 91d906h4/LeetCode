/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int compare(int* a, int* b) {
    if (*a == *b) return 0;
    else if (*a < *b) return -1;
    else return 1;
}

int* answerQueries(int* nums, int numsSize, int* queries, int queriesSize, int* returnSize) {
    int* result = malloc(sizeof(int) * queriesSize);
    *returnSize = queriesSize;

    qsort(nums, numsSize, sizeof(int), compare);

    for (int i = 0; i < queriesSize; i++) {
        int counter = 0;

        for (int j = 0; j <= numsSize; j++) {
            if (j == numsSize) {
                result[i] = counter;
            } else if (queries[i] < nums[j]) {
                result[i] = counter;
                break;
            } else {
                queries[i] -= nums[j];
                counter++;
            }
        }
    }

    return result;
}
