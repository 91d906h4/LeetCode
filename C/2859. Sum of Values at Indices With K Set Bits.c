int kbit(int a) {
    int count = 0;

    while (a != 0) {
        count += (a % 2);
        a >>= 1;
    }

    return count;
}

int sumIndicesWithKSetBits(int* nums, int numsSize, int k){
    int result = 0;

    for (int i = 0; i < numsSize; i++)
        if (kbit(i) == k)
            result += nums[i];

    return result;
}
