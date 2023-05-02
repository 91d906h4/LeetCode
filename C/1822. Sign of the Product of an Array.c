int arraySign(int* nums, int numsSize){
    int neg = 0;

    for (int i = 0; i < numsSize; i++) {
        if (*(nums + i) == 0) return 0;
        else if (*(nums + i) < 0) neg++;
    }

    return (neg % 2) ? -1 : 1;
}
