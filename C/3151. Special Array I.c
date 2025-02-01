bool isArraySpecial(int* nums, int numsSize) {
    if (numsSize == 1)
        return true;

    for (int i = 1; i < numsSize; i++) {
        if ((*(nums + i - 1) & 1) == (*(nums + i) & 1))
            return false;
    }

    return true;
}
