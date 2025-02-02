bool check(int* nums, int numsSize) {
    int gap = 0;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > nums[(i + 1) % numsSize])
            gap++;
    }

    return gap <= 1;
}
