/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findPeaks(int* mountain, int mountainSize, int* returnSize) {
    int counter = 0, ptr = 1;
    int* result = (int*)malloc(sizeof(int) * mountainSize - 2);

    while (ptr + 1 < mountainSize) {
        int* temp = mountain + ptr;

        if (*(temp - 1) < *temp && *temp > *(temp + 1))
            *(result + counter++) = ptr;

        ptr++;
    }

    *returnSize = counter;

    return result;
}
