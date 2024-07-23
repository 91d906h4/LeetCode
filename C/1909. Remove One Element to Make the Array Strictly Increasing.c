bool canBeIncreasing(int* nums, int numsSize) {
    if (numsSize <= 2)
        return true;

    int remove = 0;

    for (int i = 1; i < numsSize; i++) {
        if (remove > 1)
            return false;

        if (nums[i - 1] >= nums[i]) {
            if (
                ((i >= 2 && nums[i - 2] < nums[i]) || i == 1) || // remove i - 1
                ((i + 1 < numsSize && nums[i - 1] < nums[i + 1]) || i + 1 == numsSize) // remove i
            )
                remove++;
            else
                return false;
        }
    }

    return remove <= 1;
}
