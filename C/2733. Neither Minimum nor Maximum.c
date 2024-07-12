void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int findNonMinOrMax(int* nums, int numsSize){
    if (numsSize < 3)
        return -1;

    int min = nums[0],
        mid = nums[1],
        max = nums[2];

    if (max < min) swap(&max, &min);
    if (mid < min) swap(&mid, &min);
    if (max < mid) swap(&max, &mid);

    return mid;
}
