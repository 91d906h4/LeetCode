int peakIndexInMountainArray(int* arr, int arrSize){
    int l = 0, r = arrSize, m;

    while (l <= r) {
        m = (l + r) / 2;

        if (*(arr + m) < *(arr + m + 1)) l = m + 1;
        else r = m - 1;
    }

    return l;
}
