void nextPermutation(int* nums, int numsSize) {
    // Return if get edge cases.
    if (numsSize == 1)
        return;

    // Define variables.
    register int i = 0;
    int pivot = 0, change = 0, temp = 0;

    // Find pivot.
    for (i = numsSize - 2; i >= 0; i--) {
        if (*(nums + i) < *(nums + i + 1)) {
            pivot = i;
            break;
        }
    }

    // Find the change point.
    // (The change point is the number that has the smallest value
    // on the right side of pivot but bigger than pivot)
    int min = *(nums + pivot + 1);
    for (i = pivot + 1; i < numsSize; i++) {
        temp = *(nums + i);

        if (temp > *(nums + pivot) && temp <= min) {
            min = temp;
            change = i;
        }
    }
    
    // Return reversed array if the array is sorted in
    // reversed order.
    int tSize = numsSize - 1;
    if (pivot == 0 && change == 0) {
        for (i = 0; i < numsSize / 2; i++) {
            temp = *(nums + i);
            *(nums + i) = *(nums + tSize);
            *(nums + tSize) = temp;
            tSize--;
        }
        return;
    }

    // Change the values of pivot and the change point.
    temp = *(nums + pivot);
    *(nums + pivot) = *(nums + change);
    *(nums + change) = temp;

    // Reverse all the elements on the right side of pivot.
    tSize = numsSize - 1;
    for (i = pivot + 1; i < (numsSize + pivot + 1) / 2; i++) {
        temp = *(nums + i);
        *(nums + i) = *(nums + tSize);
        *(nums + tSize) = temp;
        tSize--;
    }
}
